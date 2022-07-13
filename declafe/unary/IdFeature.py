from typing import List, TypeGuard

import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["IdFeature"]

from .. import FeatureGen
from lib.features.composed import MinuteNFeature


class IdFeature(UnaryColumnFeature):

  @property
  def name(self) -> str:
    return "id"

  def _feature_name(self) -> str:
    return self.column_name

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser

  @staticmethod
  def many(columns: List[str]) -> List["IdFeature"]:
    return [IdFeature(c) for c in columns]

  def minute_ns(self, ns: List[int]) -> "MinuteNFeature":
    from .. import MinuteNFeature
    return [MinuteNFeature(self.column_name, n) for n in ns]

  def hour_ns(self, ns: List[int]) -> "HourNFeature":
    from .. import HourNFeature
    return [HourNFeature(self.column_name, n) for n in ns]

  def dip_againsts(self, high_column: str, max_high_periods: List[int]) -> List["FeatureGen"]:
    from lib.features.unary import IdFeature
    from lib.features.composed import DipFeature

    return [DipFeature(price_column=self.column_name, high_column=high_column, hh_period=p) for p in max_high_periods]

  def rip_againsts(self, low_column: str, min_low_periods: List[int]) -> List["FeatureGen"]:
    from lib.features.unary import IdFeature
    from lib.features.composed import RipFeature

    return [RipFeature(price_column=self.column_name, low_column=low_column, ll_period=p) for p in min_low_periods]

  @staticmethod
  def is_id(a: FeatureGen) -> TypeGuard["IdFeature"]:
    return isinstance(a, IdFeature)
