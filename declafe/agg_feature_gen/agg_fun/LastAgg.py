from typing import Any

import pandas as pd

from .AggFun import AggFun


class LastAgg(AggFun):

  def __call__(self, ser: pd.Series) -> Any:
    return ser.iat[-1]

  @property
  def fun_name(self) -> str:
    return "last"
