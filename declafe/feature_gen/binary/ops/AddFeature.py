import numpy as np

__all__ = ["AddFeature"]

from declafe.feature_gen.binary.BinaryFeature import BinaryFeature
from declafe.feature_gen.types import as_numeric


class AddFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return as_numeric(left + right)

  def _feature_name(self) -> str:
    return f"{self.left}_+_{self.right}"
