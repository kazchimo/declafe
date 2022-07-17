import pandas as pd
import talib

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["MidpointFeature"]


class MidpointFeature(UnaryColumnFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

    if self.periods < 2:
      raise ValueError("periodsは1より大きい必要があります")

  @property
  def name(self) -> str:
    return f"midpoint_{self.periods}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.MIDPOINT(ser, self.periods)
