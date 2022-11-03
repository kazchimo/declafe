import numpy as np

__all__ = ["EqFeature"]

from ..BinaryFeature import BinaryFeature


class EqFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return (left == right).astype(bool)

  def _feature_name(self) -> str:
    return f"{self.left}_==_{self.right}"
