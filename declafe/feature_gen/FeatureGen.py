from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Type, Union

import pandas as pd

__all__ = ["FeatureGen", "ColLike"]

from .ChainMixin import ChainMixin
from .ConstructorMixin import ConstructorMixin
from .OpsMixin import OpsMixin
from .types import DTypes

if TYPE_CHECKING:
  from declafe.feature_gen.Features import Features

ColLike = Union["FeatureGen", str]


class FeatureGen(ABC, ConstructorMixin, ChainMixin, OpsMixin):

  def _self(self) -> "FeatureGen":
    return self

  def __init__(self):
    super().__init__()
    self.override_feature_name: Optional[str] = None
    self.dtype: Optional[DTypes] = None

  @abstractmethod
  def gen(self, df: pd.DataFrame) -> pd.Series:
    """
    generate feature
    should be side-effect free
    """
    raise NotImplementedError

  def generate(self, df: pd.DataFrame) -> pd.Series:
    """
    optimized gen
    side-effect free
    """
    result = df[self.feature_name] \
      if self.feature_name in df.columns \
      else self.gen(df)
    return result.astype(self.dtype) if self.dtype else result

  @abstractmethod
  def _feature_name(self) -> str:
    """
    default feature name used for this FeatureGen class
    """
    raise NotImplementedError

  @property
  def feature_name(self) -> str:
    return self.override_feature_name or \
           (self._feature_name())

  def equals(self, other: "FeatureGen") -> bool:
    return self.feature_name == other.feature_name

  @property
  def to_features(self) -> "Features":
    return self._FS.one(self)

  def combine(self, other: "FeatureGen") -> "Features":
    return self.to_features.add_feature(other)

  def as_name_of(self, feature_name: str) -> "FeatureGen":
    self.override_feature_name = feature_name
    return self

  def set_feature(self, df: pd.DataFrame) -> "pd.DataFrame":
    if self.feature_name in df.columns:
      return df
    else:
      return pd.concat(
          [df, pd.DataFrame({self.feature_name: self.generate(df)})], axis=1)

  def as_type(self, dtype: DTypes) -> "FeatureGen":
    self.dtype = dtype
    return self

  @staticmethod
  def FS() -> "Type[Features]":
    from declafe.feature_gen.Features import Features
    return Features

  @property
  def _FS(self) -> "Type[Features]":
    from declafe.feature_gen.Features import Features
    return Features

  def to_col(self, c: Union["FeatureGen", str]) -> str:
    if isinstance(c, FeatureGen):
      return c.feature_name
    else:
      return c

  def __str__(self):
    return self.feature_name
