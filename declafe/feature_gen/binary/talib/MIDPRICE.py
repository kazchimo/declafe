import pandas as pd
import talib

from ..BinaryFeature import BinaryFeature

__all__ = ["MIDPRICEFeature"]


class MIDPRICEFeature(BinaryFeature):

  def __init__(self, high: str, low: str):
    super().__init__(high, low)

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.MIDPRICE(left, right)

  def _feature_name(self) -> str:
    return "MIDPRICE"
