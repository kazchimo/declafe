from typing import TYPE_CHECKING

import numpy as np
import pandas as pd
from scipy.ndimage import shift

from .UnaryFeature import UnaryFeature

__all__ = ["PctChangeFeature"]

if TYPE_CHECKING:
  from declafe import series


class PctChangeFeature(UnaryFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"pct_change_{self.periods}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    r = ser / shift(ser.astype(float), self.periods, cval=np.NaN) - 1
    return r

  @staticmethod
  def gen_target(values: "series", changes: "series") -> pd.Series:
    """変化率から実際に変化後の値を返す"""
    return values * (1 + changes)
