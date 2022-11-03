import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["MaxCompFeature"]


class MaxCompFeature(UnaryFeature):

  def __init__(self, comp: float, column_name: str):
    super().__init__(column_name)
    self.comp = comp

  @property
  def name(self) -> str:
    return f"max_comp_with_{self.comp}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return np.maximum(ser, self.comp)
