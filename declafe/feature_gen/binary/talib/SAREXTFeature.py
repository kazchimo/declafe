import numpy as np
import talib

from ..BinaryFeature import BinaryFeature


class SAREXTFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return talib.SAREXT(left.astype(float), right.astype(float))

  def _feature_name(self) -> str:
    return f"SAREXT_{self.left}_{self.right}"
