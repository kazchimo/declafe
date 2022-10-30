import pandas as pd
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

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.WMA(ser, self.periods)
