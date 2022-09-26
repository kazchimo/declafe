import pandas as pd
import talib

from ..BinaryFeature import BinaryFeature

__all__ = ["PlusDMFeature"]

from ...FeatureGen import ColLike


class PlusDMFeature(BinaryFeature):

  def __init__(self, high: ColLike, low: ColLike, period: int):
    super().__init__(high, low)
    self.period = period

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.PLUS_DM(left, right, self.period)

  def _feature_name(self) -> str:
    return f"PLUS_DM_{self.left}_{self.right}_{self.period}"
