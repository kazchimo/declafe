from dataclasses import dataclass

import pandas as pd

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["SecondFeature"]


@dataclass
class SecondFeature(UnaryColumnFeature):

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: x.second)

  @property
  def name(self) -> str:
    return f"second"
