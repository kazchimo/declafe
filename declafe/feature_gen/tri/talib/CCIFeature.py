import numpy as np
import talib

from declafe import ColLike

__all__ = ["CCIFeature"]

from declafe.feature_gen.tri.TriFeature import TriFeature


class CCIFeature(TriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike, period: int):
    super().__init__(high, low, close)
    self.period = period

  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    return talib.CCI(col1.astype(float), col2.astype(float), col3.astype(float),
                     self.period)

  def _feature_name(self) -> str:
    return f"CCI_{self.period}_of_{self.col1}_{self.col2}_{self.col3}"
