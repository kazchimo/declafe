import pandas as pd
import talib

from ..UnaryColumnFeature import UnaryColumnFeature


class T3Feature(UnaryColumnFeature):

  def __init__(self, column_name: str, period: int):
    super().__init__(column_name)
    self.period = period

  @property
  def name(self) -> str:
    return f"T3_{self.period}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.T3(ser, timeperiod=self.period)
