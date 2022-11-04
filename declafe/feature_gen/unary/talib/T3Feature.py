import numpy as np
import talib

from ..UnaryFeature import UnaryFeature


class T3Feature(UnaryFeature):

  def __init__(self, column_name: str, period: int):
    super().__init__(column_name)
    self.period = period

  @property
  def name(self) -> str:
    return f"T3_{self.period}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.T3(ser.astype(float), timeperiod=self.period)
