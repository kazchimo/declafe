import pandas as pd

from ..UnaryColumnFeature import UnaryFeature

__all__ = ["HourFeature"]


class HourFeature(UnaryFeature):

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: x.hour)

  @property
  def name(self) -> str:
    return f"hour"
