import numpy as np
import talib

from ..BinaryFeature import BinaryFeature


class SARFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return talib.SAR(left.astype(float), right.astype(float))

  def _feature_name(self) -> str:
    return f"SAR_{self.left}_{self.right}"
