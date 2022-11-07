from typing import Any

import numpy as np
import pandas as pd

from .FeatureGen import FeatureGen

__all__ = ["ConstFeature"]


class ConstFeature(FeatureGen):

  def __init__(self, const: Any):
    super().__init__()
    self.const = const

  def _gen(self, df: pd.DataFrame) -> np.ndarray:
    return np.full(len(df), self.const)

  def _feature_name(self) -> str:
    return f"{self.const}"

  @staticmethod
  def conv(a: Any) -> "FeatureGen":
    if not isinstance(a, FeatureGen):
      return ConstFeature(a)
    else:
      return a
