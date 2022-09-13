import pandas as pd

from ..BinaryFeature import BinaryFeature

__all__ = ["ModFeature"]


class ModFeature(BinaryFeature):

  def __init__(self, left: str, right: str):
    super().__init__(left, right)

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left % right

  def _feature_name(self) -> str:
    return f"{self.left}_%_{self.right}"
