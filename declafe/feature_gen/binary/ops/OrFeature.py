import numpy as np

__all__ = ["OrFeature"]

from ..BinaryFeature import BinaryFeature


class OrFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left.astype(bool) | right.astype(bool)

  def _feature_name(self) -> str:
    return f"{self.left}_|_{self.right}"
