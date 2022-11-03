import numpy as np
import talib

from declafe import ColLike
from declafe.feature_gen.tri.TriFeature import TriFeature


class STOCHFFastkFeature(TriFeature):

  def __init__(self,
               high: ColLike,
               low: ColLike,
               close: ColLike,
               fastk_period: int,
               fastd_period: int,
               fastd_matype: int = 0):
    super().__init__(high, low, close)
    self.fastk_period = fastk_period
    self.fastd_period = fastd_period
    self.fastd_matype = fastd_matype

  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    return talib.STOCHF(col1.astype(float),
                        col2.astype(float),
                        col3.astype(float),
                        fastk_period=self.fastk_period,
                        fastd_period=self.fastd_period,
                        fastd_matype=self.fastd_matype)[0]

  def _feature_name(self) -> str:
    return f"STOCHF_fastk_{self.fastk_period}_{self.fastd_period}_{self.fastd_matype}_of_{self.col1}_{self.col2}_{self.col3}"


class STOCHFFastdFeature(TriFeature):

  def __init__(self,
               high: ColLike,
               low: ColLike,
               close: ColLike,
               fastk_period: int,
               fastd_period: int,
               fastd_matype: int = 0):
    super().__init__(high, low, close)
    self.fastk_period = fastk_period
    self.fastd_period = fastd_period
    self.fastd_matype = fastd_matype

  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    return talib.STOCHF(col1.astype(float),
                        col2.astype(float),
                        col3.astype(float),
                        fastk_period=self.fastk_period,
                        fastd_period=self.fastd_period,
                        fastd_matype=self.fastd_matype)[1]

  def _feature_name(self) -> str:
    return f"STOCHF_fastd_{self.fastk_period}_{self.fastd_period}_{self.fastd_matype}_of_{self.col1}_{self.col2}_{self.col3}"
