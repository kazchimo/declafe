from typing import Union

import pandas as pd
import talib

from declafe.feature_gen import FeatureGen

__all__ = ["DXFeature"]

C = Union[FeatureGen, str]


class DXFeature(FeatureGen):

  def __init__(self, high: C, low: C, close: C, period: int):
    super().__init__()
    self.high = self.to_col(high)
    self.low = self.to_col(low)
    self.close = self.to_col(close)
    self.period = period

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return talib.DX(df[self.high], df[self.low], df[self.close], self.period)

  def _feature_name(self) -> str:
    return f"DX_{self.period}_of_{self.close}"
