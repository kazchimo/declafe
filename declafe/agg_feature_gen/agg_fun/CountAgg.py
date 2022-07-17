import pandas as pd

from .AggFun import AggFun


class CountAgg(AggFun):

  def __call__(self, ser: pd.Series) -> int:
    return ser.size

  @property
  def fun_name(self) -> str:
    return "count"
