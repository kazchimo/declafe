from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Type

import pandas as pd

__all__ = ["FeatureGen"]

from .ChainMixin import ChainMixin
from .ConstructorMixin import ConstructorMixin
from .OpsMixin import OpsMixin

if TYPE_CHECKING:
  from declafe.feature_gen.Features import Features


class FeatureGen(ABC, ConstructorMixin, ChainMixin, OpsMixin):

  def _self(self) -> "FeatureGen":
    return self

  def __init__(self):
    super().__init__()
    self.override_feature_name: Optional[str] = None

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
    if self.feature_name in df.columns:
      return df[self.feature_name]
    else:
      return self.gen(df)

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

  @staticmethod
  def FS() -> "Type[Features]":
    from declafe.feature_gen.Features import Features
    return Features

  @property
  def _FS(self) -> "Type[Features]":
    from declafe.feature_gen.Features import Features
    return Features

