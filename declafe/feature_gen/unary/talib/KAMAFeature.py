import pandas as pd
import talib

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["KAMAFeature"]


class KAMAFeature(UnaryColumnFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

    if periods <= 0:
      raise ValueError("periods must be greater than 0")

  @property
  def name(self) -> str:
    return f"kama_{self.periods}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.KAMA(ser, self.periods)
