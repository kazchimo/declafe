from dataclasses import dataclass

import pandas as pd

from declafe.unary.UnaryColumnFeature import UnaryColumnFeature

__all__ = ["DayOfWeekFeature"]

regex = "day_of_week_of_(\w+)"


@dataclass
class DayOfWeekFeature(UnaryColumnFeature):
  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: x.weekday())

  @property
  def name(self) -> str:
    return f"day_of_week"
