from abc import ABC, abstractmethod
from typing import Optional, Union, Literal, Any

from pl.feature_gen.types import DTypes
import polars as pl


class FeatureGen(ABC):

  def __init__(self):
    super(FeatureGen, self).__init__()
    self.override_feature_name: Optional[str] = None
    self.dtype: Optional[Union[DTypes, Literal["numeric_auto"]]] = None

  @abstractmethod
  def _expr(self) -> pl.Expr:
    raise NotImplementedError

  def expr(self) -> pl.Expr:
    return self._expr().alias(self.feature_name)

  def equals(self, other: "FeatureGen") -> bool:
    return self.feature_name == other.feature_name

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
           (self._feature_name())

  @abstractmethod
  def _feature_name(self) -> str:
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

  def sum(self, periods: int) -> "FeatureGen":
    from pl.feature_gen.unary.sum_feature import SumFeature
    return SumFeature(periods, self)

  def log(self) -> "FeatureGen":
    from pl.feature_gen.unary.log_feature import LogFeature
    return LogFeature(self)

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
