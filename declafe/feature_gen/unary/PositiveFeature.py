import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["IsPositiveFeature"]


class IsPositiveFeature(UnaryColumnFeature):

  @property
  def name(self) -> str:
    return f"is_positive"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser > 0
