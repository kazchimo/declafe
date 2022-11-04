import numpy as np
import talib

from ..UnaryFeature import UnaryFeature

__all__ = ["CMOFeature"]


class CMOFeature(UnaryFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"CMO_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.CMO(ser.astype(float), self.periods)
