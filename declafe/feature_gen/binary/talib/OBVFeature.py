import numpy as np
import talib

from ..BinaryFeature import BinaryFeature

__all__ = ["OBVFeature"]

from ...FeatureGen import ColLike


class OBVFeature(BinaryFeature):

  def __init__(self, close: ColLike, volume: ColLike):
    super().__init__(close, volume)

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return talib.OBV(left.astype(float), right.astype(float))

  def _feature_name(self) -> str:
    return f"OBV_{self.left}_{self.right}"
