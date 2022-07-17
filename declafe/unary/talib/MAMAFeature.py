import pandas as pd
import talib

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["MAMAFeature", "FAMAFeature"]


class MAMAFeature(UnaryColumnFeature):

  def __init__(self,
               column_name: str,
               fast_limit: float = 0.5,
               slow_limit: float = 0.05):
    super().__init__(column_name)
    self.fast_limit = fast_limit
    self.slow_limit = slow_limit

  @property
  def name(self) -> str:
    return f"mama{self.fast_limit}-{self.slow_limit}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.MAMA(ser, self.fast_limit, self.slow_limit)[0]


class FAMAFeature(UnaryColumnFeature):

  def __init__(self,
               column_name: str,
               fast_limit: float = 0.5,
               slow_limit: float = 0.05):
    super().__init__(column_name)
    self.fast_limit = fast_limit
    self.slow_limit = slow_limit

  @property
  def name(self) -> str:
    return f"fama{self.fast_limit}-{self.slow_limit}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.MAMA(ser, self.fast_limit, self.slow_limit)[1]
