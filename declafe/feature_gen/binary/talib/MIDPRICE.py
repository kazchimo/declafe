import pandas as pd
import talib

from declafe import ColLike
from ..BinaryFeature import BinaryFeature

__all__ = ["MIDPRICEFeature"]


class MIDPRICEFeature(BinaryFeature):

  def __init__(self, high: ColLike, low: ColLike, period: int):
    self.period = period
    super().__init__(high, low)

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.MIDPRICE(left, right, self.period)

  def _feature_name(self) -> str:
    return f"MIDPRICE_{self.period}_{self.left}_{self.right}"
