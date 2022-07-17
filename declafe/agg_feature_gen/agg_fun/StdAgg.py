from typing import Any

import pandas as pd

from .AggFun import AggFun


class StdAgg(AggFun):

  def __call__(self, ser: pd.Series) -> Any:
    return ser.to_numpy().std()

  @property
  def fun_name(self) -> str:
    return "std"
