from dataclasses import dataclass

import pandas as pd

__all__ = ["LEFeature"]

from ..BinaryFeature import BinaryFeature


@dataclass
class LEFeature(BinaryFeature):
  left: str
  right: str

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left <= right

  def _feature_name(self) -> str:
    return f"{self.left}_is_less_than_equal_{self.right}"
