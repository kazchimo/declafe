from typing import Any

import pandas as pd

from .AggFun import AggFun

__all__ = ["DiffAtAgg"]


class DiffAtAgg(AggFun):

  def __init__(self, target: str, at: int):
    super().__init__(target)
    self.at = at

  def __call__(self, ser: pd.Series) -> Any:
    return ser.diff(1).iloc[[self.at]]

  @property
  def fun_name(self) -> str:
    return f"diff_at{self.at}"
