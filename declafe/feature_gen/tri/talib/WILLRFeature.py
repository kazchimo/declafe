import pandas as pd
import talib

from declafe import ColLike
from declafe.feature_gen.tri.TriFeature import TriFeature


class WILLRFeature(TriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               timeperiod: int):
    super().__init__(high, low, close)
    self.timeperiod = timeperiod

  def trigen(self, col1: pd.Series, col2: pd.Series,
             col3: pd.Series) -> pd.Series:
    return talib.WILLR(col1, col2, col3, timeperiod=self.timeperiod)

  def _feature_name(self) -> str:
    return f"WILLR_{self.timeperiod}_of_{self.col1}_{self.col2}_{self.col3}"
