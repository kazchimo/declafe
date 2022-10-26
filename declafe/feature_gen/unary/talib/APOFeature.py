import pandas as pd
import talib

from ..UnaryColumnFeature import UnaryFeature

__all__ = ["APOFeature"]


class APOFeature(UnaryFeature):

  def __init__(self,
               column_name: str,
               fastperiod: int = 12,
               slowperiod: int = 26,
               matype: int = 0):
    super().__init__(column_name)
    self.fastperiod = fastperiod
    self.slowperiod = slowperiod
    self.matype = matype

  @property
  def name(self) -> str:
    return f"APO{self.fastperiod}_{self.slowperiod}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.APO(ser, self.fastperiod, self.slowperiod, self.matype)
