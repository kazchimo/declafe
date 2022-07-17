from typing import Any

import numpy as np
import pandas as pd

from .AggFun import AggFun


class NUniqueAgg(AggFun):

  def __call__(self, ser: pd.Series) -> Any:
    return np.size(np.unique(ser.to_numpy()))

  @property
  def fun_name(self) -> str:
    return "nunique"
