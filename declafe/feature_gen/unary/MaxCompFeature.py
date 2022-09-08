import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["MaxCompFeature"]


class MaxCompFeature(UnaryColumnFeature):

  def __init__(self, comp: float, column_name: str):
    super().__init__(column_name)
    self.comp = comp

  @property
  def name(self) -> str:
    return f"max_comp_with_{self.comp}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: max(x, self.comp))
