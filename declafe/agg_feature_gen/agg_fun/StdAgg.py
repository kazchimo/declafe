from typing import Any

import numpy as np
import pandas as pd

from .AggFun import AggFun


class StdAgg(AggFun):

  def __call__(self, ser: pd.Series) -> Any:
    return np.std(ser)

  @property
  def fun_name(self) -> str:
    return "std"
