import numpy as np

from .UnaryFeature import UnaryFeature
import pandas as pd

__all__ = ["MaxFeature"]


class MaxFeature(UnaryFeature):

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

    if self.periods < 2:
      raise ValueError("periodsは1より大きい必要があります")

  @property
  def name(self) -> str:
    return f"max_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return pd.Series(ser).rolling(self.periods).max().to_numpy()
