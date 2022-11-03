import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["IsPositiveFeature"]


class IsPositiveFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"is_positive"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return ser > 0
