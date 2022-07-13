from typing import Any

import pandas as pd

from lib.features.feature_gen import FeatureGen

__all__ = ["ConstFeature"]

class ConstFeature(FeatureGen):
  def __init__(self, const: Any):
    super().__init__()
    self.const = const

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return pd.Series(self.const, index=df.index)

  def _feature_name(self) -> str:
    return f"{self.const}"

  @staticmethod
  def make(a: Any):
    if not isinstance(a, FeatureGen):
      return ConstFeature(a)
    else:
      return a
