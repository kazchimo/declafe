import pandas as pd

from declafe import series
from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["PctChangeFeature"]


class PctChangeFeature(UnaryColumnFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"pct_change_{self.periods}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.pct_change(periods=self.periods)

  @staticmethod
  def gen_target(values: series, changes: series) -> pd.Series:
    """変化率から実際に変化後の値を返す"""
    return values * (1 + changes)
