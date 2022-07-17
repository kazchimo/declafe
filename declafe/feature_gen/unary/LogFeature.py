import numpy as np
import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["LogFeature"]


class LogFeature(UnaryColumnFeature):

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    if not pd.api.types.is_numeric_dtype(ser):
      raise ValueError("dTypeは数値型である必要があります")

    return np.log(ser)

  @property
  def name(self) -> str:
    return f"log"
