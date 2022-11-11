import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["MedFeature"]


class MedFeature(UnaryFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods
    if self.periods < 2:
      raise ValueError("periodsは1より大きい必要があります")

  @property
  def name(self) -> str:
    return f"med_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    p = self.periods

    @self.numba_dec
    def gen(idx: int) -> float:
      a = ser[idx - p + 1:idx + 1]

      if len(a) == 0:
        return np.nan
      else:
        return np.median(a)  # type: ignore

    return np.frompyfunc(gen, 1, 1)(np.arange(len(ser))).astype("float")
