import pandas as pd
import talib

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["BBandsUpperFeature", "BBandsLowerFeature"]


class BBandsUpperFeature(UnaryColumnFeature):

  def __init__(self, periods: int, column_name: str, nbdevup: float = 2):
    super().__init__(column_name)
    self.periods = periods
    self.nbdevup = nbdevup

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.BBANDS(ser, self.periods, self.nbdevup, 2, 0)[0]

  @property
  def name(self) -> str:
    return f"bbands_upper{self.nbdevup}_{self.periods}"


class BBandsLowerFeature(UnaryColumnFeature):

  def __init__(self, periods: int, column_name: str, nbdevdn: float = 2):
    super().__init__(column_name)
    self.periods = periods
    self.nbdevdn = nbdevdn

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.BBANDS(ser, self.periods, 2, self.nbdevdn, 0)[2]

  @property
  def name(self) -> str:
    return f"bbands_lower{self.nbdevdn}_{self.periods}"
