import numpy as np
import pandas as pd

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
    return pd.Series(ser).pct_change(self.periods).to_numpy()
