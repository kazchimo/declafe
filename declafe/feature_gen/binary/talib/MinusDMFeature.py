from typing import Union

import pandas as pd
import talib

from declafe.feature_gen import FeatureGen

__all__ = ["MinusDMFeature"]

C = Union[FeatureGen, str]


class MinusDMFeature(FeatureGen):

  def __init__(self, high: C, low: C, period: int):
    super().__init__()
    self.high = self.to_col(high)
    self.low = self.to_col(low)
    self.period = period

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return talib.MINUS_DM(df[self.high], df[self.low], self.period)

  def _feature_name(self) -> str:
    return f"MINUS_DM_{self.high}_{self.low}_{self.period}"
