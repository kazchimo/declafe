import numpy as np
import pandas as pd

from .UnaryFeature import UnaryFeature

__all__ = ["FlipBoolFeature"]


class FlipBoolFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"not"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    if not pd.api.types.is_bool_dtype(ser):
      raise ValueError("serはbool型である必要があります")

    return ~ser
