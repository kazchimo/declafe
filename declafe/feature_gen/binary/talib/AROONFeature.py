import pandas as pd
import talib

from ..BinaryFeature import BinaryFeature


class AROONDownFeature(BinaryFeature):

  def __init__(self, high: str, low: str, period: int):
    self.period = period
    super().__init__(high, low)

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.AROON(left, right, self.period)[0]

  def _feature_name(self) -> str:
    return f"AROONDown_{self.period}"


class AROONUpFeature(BinaryFeature):

  def __init__(self, high: str, low: str, period: int):
    self.period = period
    super().__init__(high, low)

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.AROON(left, right, self.period)[1]

  def _feature_name(self) -> str:
    return f"AROONUp_{self.period}"
