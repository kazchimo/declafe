from typing import Any

import pandas as pd

from .FeatureGen import FeatureGen

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
  def conv(a: Any) -> "FeatureGen":
    if not isinstance(a, FeatureGen):
      return ConstFeature(a)
    else:
      return a
