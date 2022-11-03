import numpy as np

__all__ = ["SubFeature"]

from ..BinaryFeature import BinaryFeature


class SubFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left - right

  def _feature_name(self) -> str:
    return f"{self.left}_-_{self.right}"
