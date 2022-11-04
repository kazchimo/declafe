import numpy as np
import talib

from ..UnaryFeature import UnaryFeature

__all__ = ["DEMAFeature"]


class DEMAFeature(UnaryFeature):
  """double exponential moving average"""

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"DEMA_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.DEMA(ser.astype(float), self.periods)
