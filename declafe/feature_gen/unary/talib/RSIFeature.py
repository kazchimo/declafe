import pandas as pd
import talib

from declafe import ColLike
from declafe.feature_gen.unary import UnaryColumnFeature


class RSIFeature(UnaryColumnFeature):

  def __init__(self, column_name: ColLike, period: int):
    super().__init__(column_name)
    self.period = period

  @property
  def name(self) -> str:
    return f"RSI_{self.period}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.RSI(ser, timeperiod=self.period)
