from typing import List, Dict

import pandas as pd

from .AsType import *
from .FromTypeAs import *

__all__ = ["AsTypes", "ATS"]


class AsTypes:

  def __init__(self, as_types: List[AsType]):
    self.as_types = as_types

  def set_types(self, df: pd.DataFrame) -> None:
    for as_type in self.as_types:
      as_type.set_type(df)

  @staticmethod
  def from_type(from_type: str, as_type: str) -> "AsTypes":
    return AsTypes([FromTypeAs(from_type, as_type)])

  @staticmethod
  def from_types(dict_: Dict[str, str]) -> "AsTypes":
    return AsTypes([
        FromTypeAs(from_type, as_type) for from_type, as_type in dict_.items()
    ])

  def __add__(self, other: "AsTypes") -> "AsTypes":
    return AsTypes(self.as_types + other.as_types)


ATS = AsTypes
