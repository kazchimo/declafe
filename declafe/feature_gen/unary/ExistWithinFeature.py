from typing import Any

import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["ExistWithinFeature"]

from ... import ColLike


class ExistWithinFeature(UnaryColumnFeature):

  def __init__(self, column_name: ColLike, target_value: Any, period: int):
    super().__init__(column_name)
    self.period = period
    self.target_value = target_value

  @property
  def name(self) -> str:
    return f"{self.target_value}_exist_within_{self.period}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:

    def f(x: pd.Series) -> bool:
      return self.target_value in x.values

    return ser.rolling(self.period, min_periods=1, axis=0)\
      .apply(f).astype(bool)
