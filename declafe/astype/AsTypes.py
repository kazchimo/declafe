from typing import List

import pandas as pd

from .AsType import AsType

__all__ = ["AsTypes"]


class AsTypes:

  def __init__(self, as_types: List[AsType]):
    self.as_types = as_types

  def set_types(self, df: pd.DataFrame) -> None:
    for as_type in self.as_types:
      as_type.set_type(df)

  @staticmethod
  def from_type(from_type: str, as_type: str, df: pd.DataFrame) -> "AsTypes":
    return AsTypes(
        [
            AsType(column, as_type)
            for column in df.select_dtypes(from_type).columns
        ])
