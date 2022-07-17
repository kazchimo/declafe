from typing import Any

import numpy as np
import pandas as pd

from .AggFun import AggFun

__all__ = ["DiffAtAgg"]


class DiffAtAgg(AggFun):

  def __init__(self, target: str, at: int):
    super().__init__(target)
    self.at = at

  def __call__(self, ser: pd.Series) -> Any:
    if max(abs(self.at), abs(self.at - 1)) > ser.size - 1:
      return np.NaN
    return ser.iat[self.at] - ser.iat[self.at - 1]

  @property
  def fun_name(self) -> str:
    return f"diff_at{self.at}"
