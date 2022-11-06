__all__ = ["MinWithFeature"]

import numpy as np

from declafe.feature_gen.binary.BinaryFeature import BinaryFeature
from declafe.feature_gen.types import as_numeric


class MinWithFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return as_numeric(np.minimum(left, right))

  def _feature_name(self) -> str:
    return f"{self.left}_min_with_{self.right}"
