import numpy as np
import talib

from ..UnaryFeature import UnaryFeature


class WeightedMovingAverage(UnaryFeature):
  periods: int

  def __init__(self, column_name: str, periods: int):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"wma_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.WMA(ser.astype(float), self.periods)
