import numpy as np
import talib

from ..UnaryFeature import UnaryFeature

__all__ = ["MAMAFeature", "FAMAFeature"]


class MAMAFeature(UnaryFeature):

  def __init__(self,
               column_name: str,
               fast_limit: float = 0.5,
               slow_limit: float = 0.05):
    super().__init__(column_name)
    self.fast_limit = fast_limit
    self.slow_limit = slow_limit

  @property
  def name(self) -> str:
    return f"mama{self.fast_limit}-{self.slow_limit}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.MAMA(ser.astype(float), self.fast_limit, self.slow_limit)[0]


class FAMAFeature(UnaryFeature):

  def __init__(self,
               column_name: str,
               fast_limit: float = 0.5,
               slow_limit: float = 0.05):
    super().__init__(column_name)
    self.fast_limit = fast_limit
    self.slow_limit = slow_limit

  @property
  def name(self) -> str:
    return f"fama{self.fast_limit}-{self.slow_limit}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.MAMA(ser.astype(float), self.fast_limit, self.slow_limit)[1]
