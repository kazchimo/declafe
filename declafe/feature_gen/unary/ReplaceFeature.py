from typing import TypeVar

import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["ReplaceFeature"]

T = TypeVar("T")


class ReplaceFeature(UnaryColumnFeature):

  def __init__(self, column_name: str, target_value: T, to_value: T):
    super().__init__(column_name)
    self.target_value = target_value
    self.to_value = to_value

  @property
  def name(self) -> str:
    return f"replace_with_{self.target_value}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.replace(self.target_value, self.to_value)
