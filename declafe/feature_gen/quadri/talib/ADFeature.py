import pandas as pd
import talib

from declafe import ColLike
from declafe.feature_gen.quadri.QuadriFeature import QuadriFeature


class ADFeature(QuadriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               volume: ColLike):
    super().__init__(high, low, close, volume)

  def quadrigen(self, col1: pd.Series, col2: pd.Series, col3: pd.Series,
                col4: pd.Series) -> pd.Series:
    return talib.AD(col1, col2, col3, col4)

  def _feature_name(self) -> str:
    return f"AD_{self.col1}_{self.col2}_{self.col3}_{self.col4}"
