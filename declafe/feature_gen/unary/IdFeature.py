from typing import List, TYPE_CHECKING

import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["IdFeature"]

if TYPE_CHECKING:
  from declafe import FeatureGen
  from declafe.feature_gen.Features import Features


class IdFeature(UnaryColumnFeature):

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

  def minute_n(self, n: int) -> "FeatureGen":
    gen = (IdFeature(self.column_name).minute() % n) == 0
    return gen.as_name_of(f"minute{n}")

  def minute_ns(self, ns: List[int]) -> "Features":
    return self._FS([self.minute_n(n) for n in ns])

  def hour_n(self, n: int) -> "FeatureGen":
    gen = (IdFeature(self.column_name).hour() % n) == 0
    return gen.as_name_of(f"hour{n}")

  def hour_ns(self, ns: List[int]) -> List["FeatureGen"]:
    return [self.hour_n(n) for n in ns]

  def dip_against(self, high_column: str, max_high_period: int) -> "FeatureGen":
    gen = (
            IdFeature(self.column_name) / IdFeature(high_column).moving_max(max_high_period)
          ) - 1
    return gen.as_name_of(
        f"dip_{self.column_name}_against_max{max_high_period}_of_{high_column}")

  def dip_againsts(self, high_column: str,
                   max_high_periods: List[int]) -> "Features":
    return self._FS([self.dip_against(high_column, p) for p in max_high_periods])

  def rip_against(self, low_column: str, min_low_period: int) -> "FeatureGen":
    gen = (
            IdFeature(self.column_name) / IdFeature(low_column).moving_min(min_low_period)
           ) - 1
    return gen.as_name_of(
        f"rip_{self.column_name}_against_min{min_low_period}_of_{low_column}")

  def rip_againsts(self, low_column: str,
                   min_low_periods: List[int]) -> "Features":
    return self._FS([self.rip_against(low_column, p) for p in min_low_periods])
