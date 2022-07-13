import pandas as pd

from declafe.binary.BinaryFeature import BinaryFeature
import talib


class SAREXTFeature(BinaryFeature):
  def __init__(self, high: str, low: str):
    super().__init__(high, low)

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.SAREXT(left, right)

  def _feature_name(self) -> str:
    return "SAREXT"
