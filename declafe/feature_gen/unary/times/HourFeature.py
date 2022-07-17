import pandas as pd

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["HourFeature"]


class HourFeature(UnaryColumnFeature):

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: x.hour)

  @property
  def name(self) -> str:
    return f"hour"
