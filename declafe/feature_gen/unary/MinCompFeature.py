import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["MinCompFeature"]


class MinCompFeature(UnaryFeature):

  def __init__(self, comp: float, column_name: str):
    super().__init__(column_name)
    self.comp = comp

  @property
  def name(self) -> str:
    return f"min_comp_with_{self.comp}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return np.minimum(ser, self.comp)
