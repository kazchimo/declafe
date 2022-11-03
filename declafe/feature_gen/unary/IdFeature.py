from typing import List, TYPE_CHECKING

import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["IdFeature"]

if TYPE_CHECKING:
  from declafe.feature_gen.Features import Features


class IdFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return "id"

  def _feature_name(self) -> str:
    return self.column_name

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return ser

  @classmethod
  def many(cls, columns: List[str]) -> "Features":
    return cls.FS()([IdFeature(c) for c in columns])
