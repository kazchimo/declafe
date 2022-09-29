import pandas as pd
import talib

from declafe import ColLike

__all__ = ["MinusDMFeature"]

from declafe.feature_gen.binary import BinaryFeature


class MinusDMFeature(BinaryFeature):

  def __init__(self, high: ColLike, low: ColLike, period: int):
    super().__init__(high, low)
    self.period = period

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.MINUS_DM(left, right, self.period)

  def _feature_name(self) -> str:
    return f"MINUS_DM_{self.left}_{self.right}_{self.period}"
