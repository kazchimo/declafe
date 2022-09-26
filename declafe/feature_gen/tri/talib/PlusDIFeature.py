from typing import Union

import pandas as pd
import talib

from declafe.feature_gen import FeatureGen

__all__ = ["PlusDIFeature"]

C = Union[FeatureGen, str]


class PlusDIFeature(FeatureGen):

  def __init__(self, high: C, low: C, close: C, period: int):
    super().__init__()
    self.high = self.to_col(high)
    self.low = self.to_col(low)
    self.close = self.to_col(close)
    self.period = period

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return talib.PLUS_DI(df[self.high], df[self.low], df[self.close],
                         self.period)

  def _feature_name(self) -> str:
    return f"PLUS_DI_{self.high}_{self.low}_{self.close}_{self.period}"
