from typing import Literal

import numpy as np
import pandas as pd

from declafe import ColLike
from ..UnaryFeature import UnaryFeature

Unit = Literal["D", "s", "ms", "us", "ns"]


class ToDatetimeFeature(UnaryFeature):

  def __init__(self, column_name: ColLike, unit: Unit):
    super().__init__(column_name)
    self.unit = unit

  @property
  def name(self) -> str:
    return "to_datetime"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return pd.to_datetime(ser, unit=self.unit).values
