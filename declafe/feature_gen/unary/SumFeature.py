import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["SumFeature"]


class SumFeature(UnaryColumnFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"sum_{self.periods}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.rolling(self.periods).sum()
