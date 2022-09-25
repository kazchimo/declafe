import numpy as np
import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["AbsFeature"]


class AbsFeature(UnaryColumnFeature):

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return np.abs(ser)

  def _feature_name(self) -> str:
    return f"|{self.column_name}|"

  @property
  def name(self) -> str:
    return f"abs"
