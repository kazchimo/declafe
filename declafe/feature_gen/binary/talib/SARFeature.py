import pandas as pd
import talib

from ..BinaryFeature import BinaryFeature


class SARFeature(BinaryFeature):

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.SAR(left, right)

  def _feature_name(self) -> str:
    return f"SAR_{self.left}_{self.right}"
