from abc import ABC, abstractmethod
from typing import Optional, Union, Literal, Any, TypeVar, Callable, TypeAlias, TYPE_CHECKING, Protocol
import copy

from declafe.pl.feature_gen.types import DTypes
import declafe.pl.feature_gen as fg
import polars as pl
from polars.internals.type_aliases import FillNullStrategy

if TYPE_CHECKING:
  from talib_chain import TalibChain
  from declafe.pl.feature_gen.features import Features

T = TypeVar("T")

O: TypeAlias = Union["FeatureGen", int, float, str, bool]


class FeatureGen(ABC):

  def __init__(self):
    super(FeatureGen, self).__init__()
    self.override_feature_name: Optional[str] = None
    self.dtype: Optional[Union[DTypes, Literal["numeric_auto"]]] = None
    self.sep = "_"

  @abstractmethod
  def _expr(self) -> pl.Expr:
    raise NotImplementedError

  def expr(self) -> pl.Expr:
    return self._expr().alias(self.feature_name)

  def equals(self, other: "FeatureGen") -> bool:
    return self.feature_name == other.feature_name

  def change_seperator(self, sep: str) -> "FeatureGen":
    self.sep = sep
    return self

  def __call__(self, df: pl.DataFrame) -> pl.Series:
    return self.generate(df)

  def generate(self, df: pl.DataFrame) -> pl.Series:
    try:
      result = df.lazy().select(self.expr()).collect().get_column(
          self.feature_name)
    except Exception as e:
      raise FailedToGenerate(f"Failed to generate {self.feature_name}") from e

    return result

  def transform(self, df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(self.expr())

  def set_feature(self, df: pl.DataFrame) -> pl.DataFrame:
    return self.transform(df)

  @property
  def feature_name(self) -> str:
    return self.override_feature_name or \
           (self.sep.join(self._feature_names()))

  @abstractmethod
  def _feature_names(self) -> list[str]:
    """
    default feature name used for this FeatureGen class
    """
    raise NotImplementedError

  def alias(self, name: str) -> "FeatureGen":
    cp = copy.deepcopy(self)
    cp.override_feature_name = name
    return cp

  def map_alias(self, func: Callable[[str], str]) -> "FeatureGen":
    cp = copy.deepcopy(self)
    cp.override_feature_name = func(self.feature_name)
    return cp

  def as_name_of(self, name: str) -> "FeatureGen":
    return self.alias(name)

  def extract(self, df: pl.DataFrame) -> pl.Series:
    return df[self.feature_name]

  @property
  def to_features(self) -> "Features":
    from declafe.pl.feature_gen.features import Features
    return Features.one(self)

  def combine(self, other: "FeatureGen") -> "Features":
    return self.to_features.add_feature(other)

  def con_aps(self, f: Callable[["FeatureGen"], "Features"]) -> "Features":
    return self.to_features + f(self)

  def con_ap(self, f: Callable[["FeatureGen"], "FeatureGen"]) -> "Features":
    return self.to_features.add_feature(f(self))

  def abs(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.abs_feature import AbsFeature
    return AbsFeature(self)

  def consecutive_count_of(self, target_value: Any) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.consecutive_count_feature import ConsecutiveCountFeature
    return ConsecutiveCountFeature(self, target_value)

  def lag(self, periods: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.lag_feature import LagFeature
    return LagFeature(periods, self)

  def shift(self, periods: int) -> "FeatureGen":
    return self.lag(periods)

  def pct_change(self, periods: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.pct_change_feature import PctChangeFeature
    return PctChangeFeature(periods, self)

  def rolling_sum(self, periods: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.rolling_sum_feature import RollingSumFeature
    return RollingSumFeature(periods, self)

  def sum(self, periods: int) -> "FeatureGen":
    return self.rolling_sum(periods)

  def rolling_min(self, periods: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.rolling_min_feature import RollingMinFeature
    return RollingMinFeature(periods, self)

  def min(self, periods: int) -> "FeatureGen":
    return self.rolling_min(periods)

  def rolling_max(self, periods: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.rolling_max_feature import RollingMaxFeature
    return RollingMaxFeature(periods, self)

  def max(self, periods: int) -> "FeatureGen":
    return self.rolling_max(periods)

  def rolling_median(self, periods: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.rolling_med_feature import RollingMedFeature
    return RollingMedFeature(periods, self)

  def median(self, periods: int) -> "FeatureGen":
    return self.rolling_median(periods)

  def rolling_mean(self, periods: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.rolling_mean_feature import RollingMeanFeature
    return RollingMeanFeature(periods, self)

  def mean(self, periods: int) -> "FeatureGen":
    return self.rolling_mean(periods)

  def med(self, periods: int) -> "FeatureGen":
    return self.rolling_median(periods)

  def rolling_std(self, periods: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.rolling_std_feature import RollingStdFeature
    return RollingStdFeature(periods, self)

  def std(self, periods: int) -> "FeatureGen":
    return self.rolling_std(periods)

  def minimum(self, other: Any) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.minimum_feature import MinimumFeature
    from declafe.pl.feature_gen import conv_lit
    return MinimumFeature(self, conv_lit(other))

  def maximum(self, other: Any) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.maximum_feature import MaximumFeature
    from declafe.pl.feature_gen import conv_lit
    return MaximumFeature(self, conv_lit(other))

  def log(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.log_feature import LogFeature
    return LogFeature(self)

  def round_n(self, round_digit: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.round_n_feature import RoundNFeature
    return RoundNFeature(round_digit, self)

  def replace(self, target_value: T, to_value: T) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.replace_feature import ReplaceFeature
    return ReplaceFeature(self, target_value, to_value)

  def accumulate(self, ops_name: str, ops_func: Callable[[Any, Any],
                                                         Any]) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.accumulate_feature import AccumulateFeature
    return AccumulateFeature(self, ops_name, ops_func)

  def exists_within(self, target_value: Any, periods: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.exists_within_feature import ExistsWithinFeature
    return ExistsWithinFeature(self, target_value, periods)

  def then(self, func: Callable[[pl.Series], pl.Series],
           ops_name: str) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.from_func_feature import FromFuncFeature
    return FromFuncFeature(self, func, ops_name)

  def parse_unixtime(self, unit: Literal["ns", "us", "ms", "s",
                                         "d"]) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.times.parse_unixtime_feature import ParseUnixTimeFeature
    return ParseUnixTimeFeature(self, unit)

  def day_of_month(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.times.day_of_month_feature import DayOfMonthFeature
    return DayOfMonthFeature(self)

  def day_of_week(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.times.day_of_week_feature import DayOfWeekFeature
    return DayOfWeekFeature(self)

  def week_of_year(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.times.week_of_year_feature import WeekOfYearFeature
    return WeekOfYearFeature(self)

  def hour(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.times.hour_feature import HourFeature
    return HourFeature(self)

  def month(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.times.month_feature import MonthFeature
    return MonthFeature(self)

  def minute(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.times.minute_feature import MinuteFeature
    return MinuteFeature(self)

  def second(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.times.second_feature import SecondFeature
    return SecondFeature(self)

  def of_cond(self, true: Any, false: Any) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.cond_feature import CondFeature
    from declafe.pl.feature_gen import conv_lit

    return CondFeature(self, conv_lit(true), conv_lit(false))

  def fill_null(self,
                value: Optional[Any] = None,
                storategy: Optional[FillNullStrategy] = None,
                limit: Optional[int] = None) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.fill_null_feature import FillNullFeature
    return FillNullFeature(self, value, storategy, limit)

  def fill_nan(self, value: Any) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.fill_nan_feature import FillNanFeature
    return FillNanFeature(self, value)

  class F(Protocol):

    def __call__(self, ser: pl.Series) -> Any:
      ...

  def rolling_apply(
      self,
      window: int,
      func: F,
      ops_name: str,
  ) -> "FeatureGen":
    from declafe.pl.feature_gen.rolling_apply_feature import RollingApplyFeature
    return RollingApplyFeature(self, window, func, ops_name)

  def rolling_count(self, window: int, target: Any) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.rolling_count_feature import RollingCountFeature
    return RollingCountFeature(self, window, target)

  def rolling_true_count(self, window: int) -> "FeatureGen":
    return self.rolling_count(window, True)

  def rolling_false_count(self, window: int) -> "FeatureGen":
    return self.rolling_count(window, False)

  @property
  def talib(self) -> "TalibChain":
    from declafe.pl.feature_gen.talib_chain import TalibChain
    return TalibChain(self)

  def __add__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.add_feature import AddFeature
    return AddFeature(self, fg.conv_lit(other))

  def __radd__(self, other: O) -> "FeatureGen":
    return fg.conv_lit(other).__add__(self)

  def __sub__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.sub_feature import SubFeature
    return SubFeature(self, fg.conv_lit(other))

  def __rsub__(self, other: O) -> "FeatureGen":
    return fg.conv_lit(other).__sub__(self)

  def __mul__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.mul_feature import MulFeature
    return MulFeature(self, fg.conv_lit(other))

  def __rmul__(self, other: O) -> "FeatureGen":
    return fg.conv_lit(other).__mul__(self)

  def __truediv__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.divide_feature import DivideFeature
    return DivideFeature(self, fg.conv_lit(other))

  def __rtruediv__(self, other: O) -> "FeatureGen":
    return fg.conv_lit(other).__truediv__(self)

  def __mod__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.mod_feature import ModFeature
    return ModFeature(self, fg.conv_lit(other))

  def __rmod__(self, other: O) -> "FeatureGen":
    return fg.conv_lit(other).__mod__(self)

  def __eq__(self, other: O) -> "FeatureGen":  # type: ignore
    from declafe.pl.feature_gen.binary.ops.eq_feature import EqFeature
    return EqFeature(self, fg.conv_lit(other))

  def __ne__(self, other: O) -> "FeatureGen":  # type: ignore
    from declafe.pl.feature_gen.binary.ops.ne_feature import NeFeature
    return NeFeature(self, fg.conv_lit(other))

  def __and__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.and_feature import AndFeature
    return AndFeature(self, fg.conv_lit(other))

  def __rand__(self, other: O) -> "FeatureGen":
    return fg.conv_lit(other).__and__(self)

  def __or__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.or_feature import OrFeature
    return OrFeature(self, fg.conv_lit(other))

  def __ror__(self, other: O) -> "FeatureGen":
    return fg.conv_lit(other).__or__(self)

  def __ge__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.ge_feature import GEFeature
    return GEFeature(self, fg.conv_lit(other))

  def __gt__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.gt_feature import GTFeature
    return GTFeature(self, fg.conv_lit(other))

  def __le__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.le_feature import LEFeature
    return LEFeature(self, fg.conv_lit(other))

  def __lt__(self, other: O) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.ops.lt_feature import LTFeature
    return LTFeature(self, fg.conv_lit(other))

  def __invert__(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.invert_feature import InvertFeature
    return InvertFeature(self)

  def __str__(self) -> str:
    return self.feature_name

  @property
  def wrapped_feature_name(self) -> str:
    from declafe.pl.feature_gen.const_feature import ConstFeature
    from declafe.pl.feature_gen.unary.id_feature import IdFeature

    if isinstance(self, (IdFeature, ConstFeature)):
      return self.feature_name
    else:
      return f"({self.feature_name})"


class FailedToGenerate(Exception):
  ...
