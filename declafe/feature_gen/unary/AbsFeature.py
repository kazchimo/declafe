import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["AbsFeature"]


class AbsFeature(UnaryFeature):

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return np.abs(ser)

  def _feature_name(self) -> str:
    return f"|{self.column_name}|"

  @property
  def name(self) -> str:
    return f"abs"
