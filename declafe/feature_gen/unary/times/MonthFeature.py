import pandas as pd

from ..UnaryColumnFeature import UnaryFeature

__all__ = ["MonthFeature"]


class MonthFeature(UnaryFeature):

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: x.month)

  @property
  def name(self) -> str:
    return f"month"
