__all__ = ["MaxWithFeature"]

import numpy as np

from declafe.feature_gen.binary.BinaryFeature import BinaryFeature


class MaxWithFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return np.maximum(left, right)

  def _feature_name(self) -> str:
    return f"{self.left}_max_with_{self.right}"
