import pandas as pd

__all__ = ["AsType"]

from ..astype import AsType


class ColumnAs(AsType):

  def __init__(self, column: str, as_type: str):
    self.column = column
    self.as_type = as_type

  def set_type(self, df: pd.DataFrame) -> None:
    df[self.column] = df[self.column].astype(self.as_type)
