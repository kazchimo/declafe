from typing import TypeVar

import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["ReplaceFeature"]

T = TypeVar("T")


class ReplaceFeature(UnaryFeature):

  def __init__(self, column_name: str, target_value: T, to_value: T):
    super().__init__(column_name)
    self.target_value = target_value
    self.to_value = to_value

  @property
  def name(self) -> str:
    return f"replace_{self.target_value}_to_{self.to_value}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    if np.isnan(self.target_value):
      return np.where(np.isnan(ser), self.to_value, ser)
    else:
      return np.where(ser == self.target_value, self.to_value, ser)
