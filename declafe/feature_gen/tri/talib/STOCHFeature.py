import numpy as np
import talib

from declafe import ColLike

__all__ = ["STOCHSlowdFeature"]

from declafe.feature_gen.tri.TriFeature import TriFeature


class STOCHSlowkFeature(TriFeature):

  def __init__(self,
               high: ColLike,
               low: ColLike,
               close: ColLike,
               fastk_period: int,
               slowk_period: int,
               slowd_period: int,
               slowk_matype: int = 0,
               slowd_matype: int = 0):
    super().__init__(high, low, close)
    self.fastk_period = fastk_period
    self.slowk_period = slowk_period
    self.slowd_period = slowd_period
    self.slowk_matype = slowk_matype
    self.slowd_matype = slowd_matype

  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    return talib.STOCH(col1.astype(float),
                       col2.astype(float),
                       col3.astype(float),
                       fastk_period=self.fastk_period,
                       slowk_period=self.slowk_period,
                       slowd_period=self.slowd_period,
                       slowk_matype=self.slowk_matype,
                       slowd_matype=self.slowd_matype)[0]

  def _feature_name(self) -> str:
    return f"STOCH_slowk_{self.fastk_period}_{self.slowk_period}_{self.slowd_period}_{self.slowk_matype}_" \
           f"{self.slowd_matype}_of_{self.col1}_{self.col2}_{self.col3}"


class STOCHSlowdFeature(TriFeature):

  def __init__(self,
               high: ColLike,
               low: ColLike,
               close: ColLike,
               fastk_period: int,
               slowk_period: int,
               slowd_period: int,
               slowk_matype: int = 0,
               slowd_matype: int = 0):
    super().__init__(high, low, close)
    self.fastk_period = fastk_period
    self.slowk_period = slowk_period
    self.slowd_period = slowd_period
    self.slowk_matype = slowk_matype
    self.slowd_matype = slowd_matype

  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    return talib.STOCH(col1.astype(float),
                       col2.astype(float),
                       col3.astype(float),
                       fastk_period=self.fastk_period,
                       slowk_period=self.slowk_period,
                       slowd_period=self.slowd_period,
                       slowk_matype=self.slowk_matype,
                       slowd_matype=self.slowd_matype)[1]

  def _feature_name(self) -> str:
    return f"STOCH_slowd_{self.fastk_period}_{self.slowk_period}_{self.slowd_period}_{self.slowk_matype}_" \
           f"{self.slowd_matype}_of_{self.col1}_{self.col2}_{self.col3}"
