import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["NotFeature"]

class NotFeature(UnaryColumnFeature):
  @property
  def name(self) -> str:
    return f"~"

  def _feature_name(self) -> str:
    return "~" + self.column_name

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ~ser
