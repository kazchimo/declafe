from typing import Any

import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["ExistWithinFeature"]

from ... import ColLike


class ExistWithinFeature(UnaryFeature):

  def __init__(self, column_name: ColLike, target_value: Any, period: int):
    super().__init__(column_name)
    self.period = period
    self.target_value = target_value

  @property
  def name(self) -> str:
    return f"{self.target_value}_exist_within_{self.period}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    tv = self.target_value
    p = self.period

    @self.numba_dec
    def check(idx: int) -> bool:
      return tv in ser[idx - p + 1:idx + 1]

    return np.frompyfunc(check, 1, 1)(np.arange(len(ser)))
