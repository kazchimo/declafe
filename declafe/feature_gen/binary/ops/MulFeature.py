import pandas as pd

__all__ = ["MulFeature"]

from ..BinaryFeature import BinaryFeature


class MulFeature(BinaryFeature):

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left * right

  def _feature_name(self) -> str:
    return f"{self.left}_*_{self.right}"
