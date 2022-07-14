from typing import Any

import numpy as np
import pandas as pd

from .AggFun import AggFun


class MeanAgg(AggFun):

  def __call__(self, ser: pd.Series) -> Any:
    return np.mean(ser)

  @property
  def fun_name(self) -> str:
    return "mean"
