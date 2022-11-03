import numpy as np
import talib

from declafe import ColLike
from declafe.feature_gen.quadri.QuadriFeature import QuadriFeature


class ADOSCFeature(QuadriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               volume: ColLike, fastperiod: int, slowperiod: int):
    super().__init__(high, low, close, volume)
    self.fastperiod = fastperiod
    self.slowperiod = slowperiod

  def quadrigen(self, col1: np.ndarray, col2: np.ndarray, col3: np.ndarray,
                col4: np.ndarray) -> np.ndarray:
    return talib.ADOSC(col1.astype(float),
                       col2.astype(float),
                       col3.astype(float),
                       col4.astype(float),
                       fastperiod=self.fastperiod,
                       slowperiod=self.slowperiod)

  def _feature_name(self) -> str:
    return f"ADOSC_{self.fastperiod}_{self.slowperiod}_of_{self.col1}_{self.col2}_{self.col3}_{self.col4}"
