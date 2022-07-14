from typing import Any

import numpy as np
import pandas as pd

from .AggFun import AggFun


class MaxAgg(AggFun):

  def __call__(self, ser: pd.Series) -> Any:
    return np.max(ser)

  @property
  def fun_name(self) -> str:
    return "max"
