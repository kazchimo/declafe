import numpy as np
import talib

from ..UnaryFeature import UnaryFeature


class TRIMAFeature(UnaryFeature):

  def __init__(self, column_name: str, period: int):
    super().__init__(column_name)
    self.period = period

  @property
  def name(self) -> str:
    return f"TRIMA_{self.period}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.TRIMA(ser.astype(float), timeperiod=self.period)
