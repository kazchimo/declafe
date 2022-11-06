import numpy as np

__all__ = ["MulFeature"]

from ..BinaryFeature import BinaryFeature
from ...types import as_numeric


class MulFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return as_numeric(left * right)

  def _feature_name(self) -> str:
    return f"{self.left}_*_{self.right}"
