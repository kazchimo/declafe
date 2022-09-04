import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["MinFeature"]


class MinFeature(UnaryColumnFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

    if self.periods < 2:
      raise ValueError("periodsは1より大きい必要があります")

  @property
  def name(self) -> str:
    return f"min_{self.periods}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.rolling(self.periods).min()
