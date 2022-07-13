import re

import pandas as pd

from lib.features.binary.BinaryFeature import BinaryFeature
from lib.features.feature_gen import FeatureGen

__all__ = ["ModFeature"]

regex = "(\w+)_%_(\w+)"


class ModFeature(BinaryFeature):
  def __init__(self, left: str, right: str):
    super().__init__(left, right)

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left % right

  def _feature_name(self) -> str:
    return f"{self.left} % {self.right}"

  @staticmethod
  def serial_num() -> int:
    return 33

  @staticmethod
  def parse(s: str) -> "FeatureGen":
    match = re.match(regex, s)
    if match is None:
      raise ValueError(f"{s}は正しい形式ではありません")
    return ModFeature(left=match.group(1), right=match.group(2))
