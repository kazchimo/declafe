import pandas as pd

from .UnaryColumnFeature import UnaryFeature

__all__ = ["NotFeature"]


class NotFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"~"

  def _feature_name(self) -> str:
    return "~" + self.column_name

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return (~ser).astype(bool)
