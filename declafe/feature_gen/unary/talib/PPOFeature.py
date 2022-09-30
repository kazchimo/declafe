import pandas as pd
import talib

from declafe import ColLike
from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["PPOFeature"]


class PPOFeature(UnaryColumnFeature):

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

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.PPO(ser, self.fast_period, self.slow_period, self.matype)
