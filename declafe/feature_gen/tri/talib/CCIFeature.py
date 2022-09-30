import pandas as pd
import talib

from declafe import ColLike

__all__ = ["CCIFeature"]

from declafe.feature_gen.tri.TriFeature import TriFeature


class CCIFeature(TriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike, period: int):
    super().__init__(high, low, close)
    self.period = period

  def trigen(self, col1: pd.Series, col2: pd.Series,
             col3: pd.Series) -> pd.Series:
    return talib.CCI(col1, col2, col3, self.period)

  def _feature_name(self) -> str:
    return f"CCI_{self.period}_of_{self.col1}_{self.col2}_{self.col3}"
