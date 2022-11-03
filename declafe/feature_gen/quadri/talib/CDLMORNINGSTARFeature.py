import numpy as np
import talib

from declafe import ColLike
from declafe.feature_gen.quadri.QuadriFeature import QuadriFeature

__all__ = ["CDLMORNINGSTARFeature"]


class CDLMORNINGSTARFeature(QuadriFeature):

  def __init__(
      self,
      open: ColLike,
      high: ColLike,
      low: ColLike,
      close: ColLike,
      penetration: float = 0,
  ):
    super().__init__(open, high, low, close)
    self.penetration = penetration

  def quadrigen(self, col1: np.ndarray, col2: np.ndarray, col3: np.ndarray,
                col4: np.ndarray) -> np.ndarray:
    return talib.CDLMORNINGSTAR(
        col1.astype(float),
        col2.astype(float),
        col3.astype(float),
        col4.astype(float),
        penetration=self.penetration,
    )

  def _feature_name(self) -> str:
    return f"CDLMORNINGSTAR{self.penetration}_{self.col1}_{self.col2}_{self.col3}_{self.col4}"
