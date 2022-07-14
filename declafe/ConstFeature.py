from typing import Any

import pandas as pd

from declafe.feature_gen.FeatureGen import FeatureGen

__all__ = ["ConstFeature"]


class ConstFeature(FeatureGen):

  def __init__(self, const: Any):
    super().__init__()
    self.const = const

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return pd.Series(self.const, index=df.index)

  def _feature_name(self) -> str:
    return f"{self.const}"
