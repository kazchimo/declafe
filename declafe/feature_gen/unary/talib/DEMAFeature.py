import pandas as pd
import talib

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["DEMAFeature"]


class DEMAFeature(UnaryColumnFeature):
  """double exponential moving average"""

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"DEMA_{self.periods}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.DEMA(ser, self.periods)