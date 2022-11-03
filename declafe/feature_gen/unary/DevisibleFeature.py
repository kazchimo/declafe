import numpy as np
import pandas as pd

from .UnaryFeature import UnaryFeature

__all__ = ["DevisibleFeature"]


class DevisibleFeature(UnaryFeature):

  def __init__(self, deviser: float, column_name: str):
    super().__init__(column_name)
    self.deviser = deviser

    if self.deviser == 0:
      raise ValueError("deviserは0より上である必要があります")

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    if not pd.api.types.is_numeric_dtype(ser):
      raise ValueError("dTypeは数値型である必要があります")

    return (ser / self.deviser) == 0

  @property
  def name(self) -> str:
    return f"devisible_by_{self.deviser}"
