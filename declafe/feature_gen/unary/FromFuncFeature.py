from typing import Callable

import numpy as np

from declafe.feature_gen.unary import UnaryFeature


class FromFuncFeature(UnaryFeature):

  def __init__(self, column_name: str, func: Callable[[np.ndarray], np.ndarray],
               op_name: str):
    super().__init__(column_name)
    self.func = func
    self.op_name = op_name

  @property
  def name(self) -> str:
    return self.op_name

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return self.func(ser)
