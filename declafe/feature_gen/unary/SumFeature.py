import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["SumFeature"]


class SumFeature(UnaryFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"sum_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    v = np.ones(self.periods)
    return np.concatenate([
        np.full(self.periods - 1, np.nan),
        np.convolve(ser[::-1], v, "valid")[::-1]
    ])
