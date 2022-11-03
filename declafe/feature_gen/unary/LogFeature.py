import numpy as np
import pandas as pd

from .UnaryFeature import UnaryFeature

__all__ = ["LogFeature"]


class LogFeature(UnaryFeature):

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    if not pd.api.types.is_numeric_dtype(ser):
      raise ValueError("dTypeは数値型である必要があります")

    return np.log(ser)

  @property
  def name(self) -> str:
    return f"log"
