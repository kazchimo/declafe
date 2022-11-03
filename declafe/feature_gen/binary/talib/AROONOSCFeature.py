import numpy as np
import talib

from declafe import ColLike
from ..BinaryFeature import BinaryFeature


class AROONOSCFeature(BinaryFeature):

  def __init__(self, high: ColLike, low: ColLike, period: int):
    self.period = period
    super().__init__(high, low)

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return talib.AROONOSC(left.astype(float), right.astype(float), self.period)

  def _feature_name(self) -> str:
    return f"AROONOSC_{self.period}_{self.left}_{self.right}"
