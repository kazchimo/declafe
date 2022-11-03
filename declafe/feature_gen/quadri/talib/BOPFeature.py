import numpy as np
import talib

from declafe import ColLike
from declafe.feature_gen.quadri.QuadriFeature import QuadriFeature


class BOPFeature(QuadriFeature):

  def __init__(self, open_col: ColLike, high_col: ColLike, low_col: ColLike,
               close_col: ColLike):
    super().__init__(open_col, high_col, low_col, close_col)

  def quadrigen(self, col1: np.ndarray, col2: np.ndarray, col3: np.ndarray,
                col4: np.ndarray) -> np.ndarray:
    return talib.BOP(col1.astype(float), col2.astype(float), col3.astype(float),
                     col4.astype(float))

  def _feature_name(self) -> str:
    return f"BOP_{self.col1}_{self.col2}_{self.col3}_{self.col4}"
