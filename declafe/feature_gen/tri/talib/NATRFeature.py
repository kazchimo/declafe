import numpy as np
import talib

from declafe import ColLike
from declafe.feature_gen.tri.TriFeature import TriFeature


class NATRFeature(TriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               timeperiod: int):
    super().__init__(high, low, close)
    self.timeperiod = timeperiod

  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    return talib.NATR(col1.astype(float),
                      col2.astype(float),
                      col3.astype(float),
                      timeperiod=self.timeperiod)

  def _feature_name(self) -> str:
    return f"NATR_{self.timeperiod}_of_{self.col1}_{self.col2}_{self.col3}"
