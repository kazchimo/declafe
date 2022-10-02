import pandas as pd
import talib

from declafe import ColLike
from declafe.feature_gen.tri.TriFeature import TriFeature


class TRANGEFeature(TriFeature):

  def __init__(
      self,
      high: ColLike,
      low: ColLike,
      close: ColLike,
  ):
    super().__init__(high, low, close)

  def trigen(self, col1: pd.Series, col2: pd.Series,
             col3: pd.Series) -> pd.Series:
    return talib.TRANGE(col1, col2, col3)

  def _feature_name(self) -> str:
    return f"TRANGE_{self.col1}_{self.col2}_{self.col3}"
