import numpy as np
import talib

from declafe import ColLike
from ..BinaryFeature import BinaryFeature


class AROONDownFeature(BinaryFeature):

  def __init__(self, high: ColLike, low: ColLike, period: int):
    self.period = period
    super().__init__(high, low)

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return talib.AROON(left.astype(float), right.astype(float), self.period)[0]

  def _feature_name(self) -> str:
    return f"AROONDown_{self.period}_{self.left}_{self.right}"


class AROONUpFeature(BinaryFeature):

  def __init__(self, high: ColLike, low: ColLike, period: int):
    self.period = period
    super().__init__(high, low)

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return talib.AROON(left.astype(float), right.astype(float), self.period)[1]

  def _feature_name(self) -> str:
    return f"AROONUp_{self.period}_{self.left}_{self.right}"
