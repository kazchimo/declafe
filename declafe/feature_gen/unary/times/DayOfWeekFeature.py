import pandas as pd

from ..UnaryColumnFeature import UnaryFeature

__all__ = ["DayOfWeekFeature"]


class DayOfWeekFeature(UnaryFeature):

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: x.weekday())

  @property
  def name(self) -> str:
    return f"day_of_week"
