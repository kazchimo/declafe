import pandas as pd
import talib

from declafe import ColLike
from declafe.feature_gen.quadri.QuadriFeature import QuadriFeature


class BOPFeature(QuadriFeature):

  def __init__(self, open_col: ColLike, high_col: ColLike, low_col: ColLike,
               close_col: ColLike):
    super().__init__(open_col, high_col, low_col, close_col)

  def quadrigen(self, col1: pd.Series, col2: pd.Series, col3: pd.Series,
                col4: pd.Series) -> pd.Series:
    return talib.BOP(col1, col2, col3, col4)

  def _feature_name(self) -> str:
    return f"BOP_{self.col1}_{self.col2}_{self.col3}_{self.col4}"
