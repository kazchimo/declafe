from typing import Union

import pandas as pd
import talib

from declafe.feature_gen import FeatureGen

C = Union[FeatureGen, str]


class MFIFeature(FeatureGen):

  def __init__(self, high: C, low: C, close: C, volume: C, period: int):
    super().__init__()
    self.high = self.to_col(high)
    self.low = self.to_col(low)
    self.close = self.to_col(close)
    self.volume = self.to_col(volume)
    self.period = period

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return talib.MFI(df[self.high], df[self.low], df[self.close],
                     df[self.volume], self.period)

  def _feature_name(self) -> str:
    return f"MFI_{self.high}_{self.low}_{self.close}_{self.volume}_{self.period}"
