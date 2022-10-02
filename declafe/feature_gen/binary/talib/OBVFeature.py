import pandas as pd
import talib

from ..BinaryFeature import BinaryFeature

__all__ = ["OBVFeature"]

from ...FeatureGen import ColLike


class OBVFeature(BinaryFeature):

  def __init__(self, close: ColLike, volume: ColLike):
    super().__init__(close, volume)

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.OBV(left, right)

  def _feature_name(self) -> str:
    return f"OBV_{self.left}_{self.right}"
