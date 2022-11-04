import numpy as np

__all__ = ["AndFeature"]

from ..BinaryFeature import BinaryFeature


class AndFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left.astype(bool) & right.astype(bool)

  def _feature_name(self) -> str:
    return f"{self.left}_&_{self.right}"
