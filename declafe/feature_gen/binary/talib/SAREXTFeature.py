import pandas as pd
import talib

from ..BinaryFeature import BinaryFeature


class SAREXTFeature(BinaryFeature):

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return talib.SAREXT(left, right)

  def _feature_name(self) -> str:
    return f"SAREXT_{self.left}_{self.right}"
