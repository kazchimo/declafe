import pandas as pd
import talib

from declafe import ColLike
from declafe.feature_gen.quadri.QuadriFeature import QuadriFeature


class MFIFeature(QuadriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               volume: ColLike, period: int):
    super().__init__(high, low, close, volume)
    self.period = period

  def quadrigen(self, col1: pd.Series, col2: pd.Series, col3: pd.Series,
                col4: pd.Series) -> pd.Series:
    return talib.MFI(col1, col2, col3, col4, self.period)

  def _feature_name(self) -> str:
    return f"MFI_{self.period}_of_{self.col1}_{self.col2}_{self.col3}_{self.col4}"
