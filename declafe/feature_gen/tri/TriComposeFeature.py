from typing import Type, Dict, Any, Optional, cast
import numpy as np
import pandas as pd

from declafe.feature_gen import FeatureGen

from .TriFeature import TriFeature
from ..unary import IdFeature
from ... import ConstFeature

__all__ = ["TriComposeFeature"]


class TriComposeFeature(FeatureGen):

  def __init__(self,
               f1: FeatureGen,
               f2: FeatureGen,
               f3: FeatureGen,
               to: Type[TriFeature],
               toKwargs: Optional[Dict[str, Any]] = None):
    super().__init__()
    self.f1 = f1
    self.f2 = f2
    self.f3 = f3
    self.to = to
    self.toKwargs = toKwargs or {}

  def _gen(self, df: pd.DataFrame) -> np.ndarray:
    f1 = self.f1.generate(df)
    f2 = self.f2.generate(df)
    f3 = self.f3.generate(df)

    return self.to_instance().trigen(f1, f2, f3)

  def _feature_name(self) -> str:
    return self.to_instance().feature_name

  def to_instance(self):
    gen = self.to(col1=self.f1.feature_name,
                  col2=self.f2.feature_name,
                  col3=self.f3.feature_name,
                  **self.toKwargs)
    f1_name = self.__wrap_name(self.f1)
    f2_name = self.__wrap_name(self.f2)
    f3_name = self.__wrap_name(self.f3)
    name = gen.feature_name\
      .replace(self.f1.feature_name, f1_name)\
      .replace( self.f2.feature_name, f2_name)\
      .replace(self.f3.feature_name, f3_name)

    return cast(TriFeature, gen.as_name_of(name))

  def __wrap_name(self, f: FeatureGen):
    return f"({f.feature_name})" \
      if not isinstance(f, (ConstFeature, IdFeature)) \
      else f.feature_name

  @staticmethod
  def make(f1: FeatureGen,
           f2: FeatureGen,
           f3: FeatureGen,
           to: Type[TriFeature],
           toKwargs: Optional[Dict[str, Any]] = None) -> "FeatureGen":
    from ..unary import IdFeature

    if isinstance(f1, IdFeature) and isinstance(f2, IdFeature) and isinstance(
        f3, IdFeature):
      return to(col1=f1.feature_name,
                col2=f2.feature_name,
                col3=f3.feature_name,
                **(toKwargs or {}))
    else:
      return TriComposeFeature(f1, f2, f3, to, toKwargs)
