import numpy as np
import talib

from declafe import ColLike
from ..UnaryFeature import UnaryFeature

__all__ = ["PPOFeature"]


class PPOFeature(UnaryFeature):

  def __init__(self,
               column_name: ColLike,
               fast_period: int,
               slow_period: int,
               matype: int = 0):
    super().__init__(column_name)
    self.fast_period = fast_period
    self.slow_period = slow_period
    self.matype = matype

  @property
  def name(self) -> str:
    return f"PPO_{self.fast_period}_{self.slow_period}_{self.matype}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.PPO(ser.astype(float), self.fast_period, self.slow_period,
                     self.matype)
