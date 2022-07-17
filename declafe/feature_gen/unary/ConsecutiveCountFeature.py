from typing import Any

import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["ConsecutiveCountFeature"]


class ConsecutiveCountFeature(UnaryColumnFeature):
  """対象値の連続数を返す"""

  def __init__(self, column_name: str, target_value: Any = 1):
    super().__init__(column_name)
    self.target_value = target_value

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    """see: https://stackoverflow.com/questions/27626542/counting-consecutive-positive-values-in-python-pandas-array"""
    ser = (ser == self.target_value)
    return ser * (ser.groupby((ser != ser.shift()).cumsum()).cumcount() + 1)

  @property
  def name(self) -> str:
    return f"consecutive_count_{self.target_value}"
