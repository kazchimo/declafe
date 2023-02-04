from abc import ABC, abstractmethod
from typing import Optional, Union, Literal, Any, TypeVar

from pl.feature_gen.types import DTypes
import polars as pl

T = TypeVar("T")


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
      result = df.select(self.expr()).get_column(self.feature_name)
    except Exception as e:
      raise FailedToGenerate(f"Failed to generate {self.feature_name}") from e

    return result

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
    self.override_feature_name = name
    return self

  def as_name_of(self, name: str) -> "FeatureGen":
    return self.alias(name)

  def abs(self) -> "FeatureGen":
    from pl.feature_gen.unary.abs_feature import AbsFeature
    return AbsFeature(self)

  def consecutive_count_of(self, target_value: Any) -> "FeatureGen":
    from pl.feature_gen.unary.consecutive_count_feature import ConsecutiveCountFeature
    return ConsecutiveCountFeature(self, target_value)

  def lag(self, periods: int) -> "FeatureGen":
    from pl.feature_gen.unary.lag_feature import LagFeature
    return LagFeature(periods, self)

  def shift(self, periods: int) -> "FeatureGen":
    return self.lag(periods)

  def pct_change(self, periods: int) -> "FeatureGen":
    from pl.feature_gen.unary.pct_change_feature import PctChangeFeature
    return PctChangeFeature(periods, self)

  def rolling_sum(self, periods: int) -> "FeatureGen":
    from pl.feature_gen.unary.rolling_sum_feature import RollingSumFeature
    return RollingSumFeature(periods, self)

  def sum(self, periods: int) -> "FeatureGen":
    return self.rolling_sum(periods)

  def rolling_min(self, periods: int) -> "FeatureGen":
    from pl.feature_gen.unary.rolling_min_feature import RollingMinFeature
    return RollingMinFeature(periods, self)

  def min(self, periods: int) -> "FeatureGen":
    return self.rolling_min(periods)

  def rolling_max(self, periods: int) -> "FeatureGen":
    from pl.feature_gen.unary.rolling_max_feature import RollingMaxFeature
    return RollingMaxFeature(periods, self)

  def max(self, periods: int) -> "FeatureGen":
    return self.rolling_max(periods)

  def rolling_median(self, periods: int) -> "FeatureGen":
    from pl.feature_gen.unary.rolling_med_feature import RollingMedFeature
    return RollingMedFeature(periods, self)

  def median(self, periods: int) -> "FeatureGen":
    return self.rolling_median(periods)

  def rolling_mean(self, periods: int) -> "FeatureGen":
    from pl.feature_gen.unary.rolling_mean_feature import RollingMeanFeature
    return RollingMeanFeature(periods, self)

  def mean(self, periods: int) -> "FeatureGen":
    return self.rolling_mean(periods)

  def med(self, periods: int) -> "FeatureGen":
    return self.rolling_median(periods)

  def rolling_std(self, periods: int) -> "FeatureGen":
    from pl.feature_gen.unary.rolling_std_feature import RollingStdFeature
    return RollingStdFeature(periods, self)

  def std(self, periods: int) -> "FeatureGen":
    return self.rolling_std(periods)

  def minimum(self, comp: float) -> "FeatureGen":
    from pl.feature_gen.unary.minimum_feature import MinimumFeature
    return MinimumFeature(self, comp)

  def log(self) -> "FeatureGen":
    from pl.feature_gen.unary.log_feature import LogFeature
    return LogFeature(self)

  def round_n(self, round_digit: int) -> "FeatureGen":
    from pl.feature_gen.unary.round_n_feature import RoundNFeature
    return RoundNFeature(round_digit, self)

  def replace(self, target_value: T, to_value: T) -> "FeatureGen":
    from pl.feature_gen.unary.replace_feature import ReplaceFeature
    return ReplaceFeature(self, target_value, to_value)

  def __invert__(self) -> "FeatureGen":
    from pl.feature_gen.unary.invert_feature import InvertFeature
    return InvertFeature(self)

  @property
  def wrapped_feature_name(self) -> str:
    from pl.feature_gen.const_feature import ConstFeature
    from pl.feature_gen.unary.id_feature import IdFeature

    if isinstance(self, (IdFeature, ConstFeature)):
      return self.feature_name
    else:
      return f"({self.feature_name})"


class FailedToGenerate(Exception):
  ...
