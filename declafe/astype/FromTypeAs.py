import pandas as pd

from .AsTypes import AsType

__all__ = ["FromTypeAs"]


class FromTypeAs(AsType):

  def __init__(self, from_type: str, as_type: str):
    self.from_type = from_type
    self.as_type = as_type

  def set_type(self, df: pd.DataFrame) -> None:
    columns = df.select_dtypes(self.from_type).columns
    df[columns] = df[columns].astype(self.as_type)
