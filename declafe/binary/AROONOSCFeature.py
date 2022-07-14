import pandas as pd

from declafe.binary.BinaryFeature import BinaryFeature
import talib


class AROONOSCFeature(BinaryFeature):

  def __init__(self, high: str, low: str, period: int):
    self.period = period
    super().__init__(high, low)

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.AROONOSC(left, right, self.period)

  def _feature_name(self) -> str:
    return f"AROONOSC_{self.period}"
