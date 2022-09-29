import pandas as pd

from ..BinaryFeature import BinaryFeature

__all__ = ["ModFeature"]


class ModFeature(BinaryFeature):

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left % right

  def _feature_name(self) -> str:
    return f"{self.left}_%_{self.right}"
