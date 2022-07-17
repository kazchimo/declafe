from dataclasses import dataclass

import pandas as pd

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["DayOfMonthFeature"]


@dataclass
class DayOfMonthFeature(UnaryColumnFeature):

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: x.day)

  @property
  def name(self) -> str:
    return f"day_of_month"
