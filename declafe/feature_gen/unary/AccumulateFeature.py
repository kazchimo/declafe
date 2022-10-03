from typing import Callable, Any

import numpy as np
import pandas as pd

from declafe import ColLike
from declafe.feature_gen.unary import UnaryColumnFeature


class AccumulateFeature(UnaryColumnFeature):

  def __init__(self, column_name: ColLike, ops_name: str,
               ops_func: Callable[[Any, Any], Any]):
    super().__init__(column_name)
    self.ops_name = ops_name
    self.ops_func = ops_func

  @property
  def name(self) -> str:
    return f"accumulate_{self.ops_name}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return np.frompyfunc(self.ops_func, 2, 1).accumulate(ser)
