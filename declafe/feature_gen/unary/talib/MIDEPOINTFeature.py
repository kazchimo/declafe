import numpy as np
import talib

from ..UnaryFeature import UnaryFeature

__all__ = ["MidpointFeature"]


class MidpointFeature(UnaryFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

    if self.periods < 2:
      raise ValueError("periodsは1より大きい必要があります")

  @property
  def name(self) -> str:
    return f"midpoint_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.MIDPOINT(ser.astype(float), self.periods)
