import numpy as np
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

  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    return talib.TRANGE(col1.astype(float), col2.astype(float),
                        col3.astype(float))

  def _feature_name(self) -> str:
    return f"TRANGE_{self.col1}_{self.col2}_{self.col3}"
