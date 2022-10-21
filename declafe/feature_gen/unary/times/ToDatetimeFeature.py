from typing import Literal

import pandas as pd

from declafe import ColLike
from ..UnaryColumnFeature import UnaryColumnFeature

Unit = Literal["D", "s", "ms", "us", "ns"]


class ToDatetimeFeature(UnaryColumnFeature):

  def __init__(self, column_name: ColLike, unit: Unit):
    super().__init__(column_name)
    self.unit = unit

  @property
  def name(self) -> str:
    return "to_datetime"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return pd.to_datetime(ser, unit=self.unit)
