import numpy as np
import pandas as pd
from numba import jit

from .UnaryFeature import UnaryFeature

__all__ = ["MaxFeature"]


class MaxFeature(UnaryFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

    if self.periods < 2:
      raise ValueError("periodsは1より大きい必要があります")

  @property
  def name(self) -> str:
    return f"max_{self.periods}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    p = self.periods

    @jit(nopython=True)
    def gen(idx: int) -> float:
      a = ser[idx - p + 1:idx + 1]

      if len(a) == 0:
        return np.nan
      else:
        return max(a)

    return np.frompyfunc(gen, 1, 1)(np.arange(len(ser))).astype("float")
