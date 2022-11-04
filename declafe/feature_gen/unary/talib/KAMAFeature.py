import numpy as np
import talib

from ..UnaryFeature import UnaryFeature

__all__ = ["KAMAFeature"]


class KAMAFeature(UnaryFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

    if periods <= 0:
      raise ValueError("periods must be greater than 0")

  @property
  def name(self) -> str:
    return f"kama_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.KAMA(ser.astype(float), self.periods)
