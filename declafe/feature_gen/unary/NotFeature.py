import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["NotFeature"]


class NotFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"~"

  def _feature_name(self) -> str:
    return "~" + self.column_name

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return (~ser.astype(bool))
