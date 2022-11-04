import numpy as np
import talib

from ..UnaryFeature import UnaryFeature

__all__ = ["EMAFeature"]


class EMAFeature(UnaryFeature):
  """exponential moving average"""

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"EMA_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.EMA(ser.astype(float), self.periods)
