import numpy as np

from ..BinaryFeature import BinaryFeature

__all__ = ["ModFeature"]


class ModFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left % right

  def _feature_name(self) -> str:
    return f"{self.left}_%_{self.right}"
