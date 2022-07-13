import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["SubConstFeature"]

class SubConstFeature(UnaryColumnFeature):
  def __init__(self, const: float, column_name: str):
    self.const = const
    super().__init__(column_name=column_name)

  @property
  def name(self) -> str:
    return f"-{self.const}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser - self.const
