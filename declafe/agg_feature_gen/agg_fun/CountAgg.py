import numpy as np
import pandas as pd

from .AggFun import AggFun


class CountAgg(AggFun):

  def __call__(self, ser: pd.Series) -> int:
    return np.size(ser)

  @property
  def fun_name(self) -> str:
    return "count"
