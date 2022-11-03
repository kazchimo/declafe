import numpy as np
import talib

from ..BinaryFeature import BinaryFeature

__all__ = ["PlusDMFeature"]

from ...FeatureGen import ColLike


class PlusDMFeature(BinaryFeature):

  def __init__(self, high: ColLike, low: ColLike, period: int):
    super().__init__(high, low)
    self.period = period

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return talib.PLUS_DM(left.astype(float), right.astype(float), self.period)

  def _feature_name(self) -> str:
    return f"PLUS_DM_{self.left}_{self.right}_{self.period}"
