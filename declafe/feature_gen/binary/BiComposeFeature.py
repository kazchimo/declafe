from typing import Type, Dict, Any, Optional, cast

import numpy as np
import pandas as pd

from declafe.feature_gen import FeatureGen

__all__ = ["BiComposeFeature"]

from .BinaryFeature import BinaryFeature
from ..unary import IdFeature
from ... import ConstFeature


class BiComposeFeature(FeatureGen):

  def __init__(self,
               left: FeatureGen,
               right: FeatureGen,
               to: Type[BinaryFeature],
               toKwargs: Optional[Dict[str, Any]] = None):
    super().__init__()
    self.left = left
    self.right = right
    self.to = to
    self.toKwargs = toKwargs or {}

  def _gen(self, df: pd.DataFrame) -> np.ndarray:
    left = self.left.generate(df)
    right = self.right.generate(df)
    return self.to_instance().bigen(left, right)

  def _feature_name(self) -> str:
    return self.to_instance().feature_name

  def to_instance(self):
    gen = self.to(left=self.left.feature_name,
                  right=self.right.feature_name,
                  **self.toKwargs)
    left_name = self.__wrap_name(self.left)
    right_name = self.__wrap_name(self.right)

    return cast(
        BinaryFeature,
        gen.as_name_of(
            gen.feature_name.replace(self.left.feature_name,
                                     left_name).replace(self.right.feature_name,
                                                        right_name)))

  def __wrap_name(self, f: FeatureGen):
    return f"({f.feature_name})" \
      if not isinstance(f, (ConstFeature, IdFeature)) \
      else f.feature_name

  @staticmethod
  def make(left: FeatureGen,
           right: FeatureGen,
           to: Type[BinaryFeature],
           toKwargs: Optional[Dict[str, Any]] = None) -> "FeatureGen":
    from ..unary import IdFeature
    if isinstance(left, IdFeature) and isinstance(right, IdFeature):
      return to(left=left.column_name,
                right=right.column_name,
                **(toKwargs or {}))
    else:
      return BiComposeFeature(left, right, to, toKwargs)
