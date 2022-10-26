from typing import List, TYPE_CHECKING

import pandas as pd

from .UnaryColumnFeature import UnaryFeature

__all__ = ["IdFeature"]

if TYPE_CHECKING:
  from declafe import FeatureGen
  from declafe.feature_gen.Features import Features


class IdFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return "id"

  def _feature_name(self) -> str:
    return self.column_name

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser

  @classmethod
  def many(cls, columns: List[str]) -> "Features":
    return cls.FS()([IdFeature(c) for c in columns])
