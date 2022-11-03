import numpy as np
import talib

from declafe import ColLike
from declafe.feature_gen.tri.TriFeature import TriFeature


class ULTOSCFeature(TriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               timeperiod1: int, timeperiod2: int, timeperiod3: int):
    super().__init__(high, low, close)
    self.timeperiod1 = timeperiod1
    self.timeperiod2 = timeperiod2
    self.timeperiod3 = timeperiod3

  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    return talib.ULTOSC(col1.astype(float),
                        col2.astype(float),
                        col3.astype(float),
                        timeperiod1=self.timeperiod1,
                        timeperiod2=self.timeperiod2,
                        timeperiod3=self.timeperiod3)

  def _feature_name(self) -> str:
    return f"ULTOSC_{self.timeperiod1}_{self.timeperiod2}_{self.timeperiod3}_of_{self.col1}_{self.col2}_{self.col3}"
