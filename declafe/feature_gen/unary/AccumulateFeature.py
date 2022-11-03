from typing import Callable, Any

import numpy as np

from declafe import ColLike
from declafe.feature_gen.unary import UnaryFeature


class AccumulateFeature(UnaryFeature):

  def __init__(self, column_name: ColLike, ops_name: str,
               ops_func: Callable[[Any, Any], Any]):
    super().__init__(column_name)
    self.ops_name = ops_name
    self.ops_func = ops_func

  @property
  def name(self) -> str:
    return f"accumulate_{self.ops_name}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return np.frompyfunc(self.ops_func, 2, 1).accumulate(ser)
