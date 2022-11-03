import numpy as np
import talib

from declafe import ColLike
from declafe.feature_gen.unary import UnaryFeature


class RSIFeature(UnaryFeature):

  def __init__(self, column_name: ColLike, period: int):
    super().__init__(column_name)
    self.period = period

  @property
  def name(self) -> str:
    return f"RSI_{self.period}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.RSI(ser.astype(float), timeperiod=self.period)
