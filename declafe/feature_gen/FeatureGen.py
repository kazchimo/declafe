from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Any

import pandas as pd

__all__ = ["FeatureGen", "FG"]

from declafe.feature_gen.ChainMixin import ChainMixin
from declafe.feature_gen.ConstructorMixin import ConstructorMixin

if TYPE_CHECKING:
  from declafe import Features


class FeatureGen(ABC, ConstructorMixin, ChainMixin):

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
    from declafe import Features
    return Features.one(self)

  def to_features_with(self, other: "FeatureGen") -> "Features":
    return self.to_features.add_feature(other)

  def as_name_of(self, feature_name: str) -> "FeatureGen":
    self.override_feature_name = feature_name
    return self

  def set_feature(self, df: pd.DataFrame) -> None:
    df[self.feature_name] = self.generate(df)

  def __eq__(self, other):
    from declafe.binary import EqualFeature, BiComposeFeature

    return BiComposeFeature.make(
        left=self, right=self.__conv_const(other), to=EqualFeature)

  def __ne__(self, other):
    return (self == other).flip_bool()

  def __add__(self, other):
    from declafe.binary import AddFeature
    from declafe.binary import BiComposeFeature
    return BiComposeFeature.make(left=self, right=other, to=AddFeature)

  def __sub__(self, other):
    from declafe.binary import BiComposeFeature
    from declafe.binary import SubFeature

    return BiComposeFeature.make(self, self.__conv_const(other), SubFeature)

  def __mul__(self, other):
    from declafe.binary import BiComposeFeature
    from declafe.binary import ProductFeature

    return BiComposeFeature.make(self, self.__conv_const(other), ProductFeature)

  def __mod__(self, other):
    from declafe.binary import BiComposeFeature
    from declafe.binary import ModFeature

    return BiComposeFeature.make(self, self.__conv_const(other), ModFeature)

  def __truediv__(self, other: "FeatureGen") -> "FeatureGen":
    from declafe.binary import BiComposeFeature
    from declafe.binary import DivideFeature

    return BiComposeFeature.make(self, self.__conv_const(other), DivideFeature)

  def __gt__(self, other):
    from declafe.binary import BiComposeFeature
    from declafe.binary import IsGreaterFeature

    return BiComposeFeature.make(
        self, self.__conv_const(other), IsGreaterFeature)

  def __lt__(self, other):
    from declafe.binary import BiComposeFeature
    from declafe.binary import IsLessFeature

    return BiComposeFeature.make(self, self.__conv_const(other), IsLessFeature)

  def __ge__(self, other):
    from declafe.binary import BiComposeFeature
    from declafe.binary import GEFeature

    return BiComposeFeature.make(self, self.__conv_const(other), GEFeature)

  def __le__(self, other):
    from declafe.binary import BiComposeFeature
    from declafe.binary import LEFeature

    return BiComposeFeature.make(self, self.__conv_const(other), LEFeature)

  def __conv_const(self, con: Any):
    from declafe.dsl import c

    if not isinstance(con, FeatureGen):
      return c(con)
    else:
      return con


FG = FeatureGen
