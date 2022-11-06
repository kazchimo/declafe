import numpy as np

__all__ = ["DivideFeature"]

from declafe import ColLike
from ..BinaryFeature import BinaryFeature
from ...types import as_numeric


class DivideFeature(BinaryFeature):

  def __init__(self, left: ColLike, right: ColLike, avoid_zero=True):
    super().__init__(left, right)
    self.avoid_zero = avoid_zero

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    if self.avoid_zero:
      right = np.where(right == 0, 1e-10, right)

    if (right == 0).any():
      raise ValueError(f"{self.right} contains 0.")

    return as_numeric(left / right)

  def _feature_name(self) -> str:
    return f"{self.left}_/_{self.right}"
