import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["PctChangeFeature"]


class PctChangeFeature(UnaryFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"pct_change_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    p = self.periods
    s = ser

    @self.numba_dec
    def gen(idx: int) -> float:
      pre_idx = idx - p

      if 0 <= pre_idx < len(s):
        return s[idx] / s[pre_idx] - 1
      else:
        return np.nan

    f = np.frompyfunc(gen, 1, 1)

    return f(np.arange(len(ser))).astype("float")
