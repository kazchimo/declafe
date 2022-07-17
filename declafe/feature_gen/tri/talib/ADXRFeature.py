import pandas as pd
import talib

from declafe.feature_gen import FeatureGen


class ADXRFeature(FeatureGen):

  def __init__(self, high: str, low: str, close: str, period: int):
    super().__init__()
    self.high = high
    self.low = low
    self.close = close
    self.period = period

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return talib.ADXR(df[self.high], df[self.low], df[self.close], self.period)

  def _feature_name(self) -> str:
    return f"ADXR_{self.period}_of_{self.close}"
