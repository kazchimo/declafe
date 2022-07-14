import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["StddevFeature"]


class StddevFeature(UnaryColumnFeature):

  def __init__(self, periods: int, column_name: str, ddof: int = 1):
    super().__init__(column_name)
    self.periods = periods
    self.ddof = ddof

  def __post_init__(self):
    if self.periods < 2:
      raise ValueError("periodsは1より大きい必要があります")

  @property
  def name(self) -> str:
    return f"stdN-{self.ddof}_{self.periods}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.rolling(self.periods).std(self.ddof)
