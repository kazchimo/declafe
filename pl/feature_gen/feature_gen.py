from abc import ABC, abstractmethod
from typing import Optional, Union, Literal
import polars as pl

from pl.feature_gen.types import DTypes


class FeatureGen(ABC):

  def __init__(self):
    super(FeatureGen, self).__init__()
    self.override_feature_name: Optional[str] = None
    self.dtype: Optional[Union[DTypes, Literal["numeric_auto"]]] = None

  @abstractmethod
  def _gen(self, df: pl.DataFrame) -> pl.Series:
    raise NotImplementedError

  def __call__(self, df: pl.DataFrame) -> pl.Series:
    return self.generate(df)

  def generate(self, df: pl.DataFrame) -> pl.Series:
    """
    optimized gen
    """

    try:
      result = df[self.feature_name] \
        if self.feature_name in df.columns \
        else self._gen(df)

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


class FailedToGenerate(Exception):
  ...
