from typing import Any

import pandas as pd

from .AggFun import AggFun


class MinAgg(AggFun):

  def __call__(self, ser: pd.Series) -> Any:
    return ser.to_numpy().min()

  @property
  def fun_name(self) -> str:
    return "min"
