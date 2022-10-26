import pandas as pd
import talib

from ..UnaryColumnFeature import UnaryFeature

__all__ = ["BBandsUpperFeature", "BBandsLowerFeature"]


class BBandsUpperFeature(UnaryFeature):

  def __init__(self,
               periods: int,
               column_name: str,
               nbdevup: float,
               matype: int = 0):
    super().__init__(column_name)
    self.periods = periods
    self.nbdevup = nbdevup
    self.matype = matype

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.BBANDS(ser, self.periods, self.nbdevup, 2, self.matype)[0]

  @property
  def name(self) -> str:
    return f"bbands_upper{self.nbdevup}_{self.periods}"


class BBandsLowerFeature(UnaryFeature):

  def __init__(self,
               periods: int,
               column_name: str,
               nbdevdn: float,
               matype: int = 0):
    super().__init__(column_name)
    self.periods = periods
    self.nbdevdn = nbdevdn
    self.matype = matype

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.BBANDS(ser, self.periods, 2, self.nbdevdn, self.matype)[2]

  @property
  def name(self) -> str:
    return f"bbands_lower{self.nbdevdn}_{self.periods}"
