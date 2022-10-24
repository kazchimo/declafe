from abc import abstractmethod
from typing import Union, TYPE_CHECKING, Any

if TYPE_CHECKING:
  from declafe.feature_gen.Features import Features
  from ..feature_gen import FeatureGen

C = Union["FeatureGen", str]


class ComplexFeatureMixin:

  @abstractmethod
  def _self(self) -> "FeatureGen":
    raise NotImplementedError

  @staticmethod
  def _conv(a: Any):
    from declafe.feature_gen.ConstFeature import ConstFeature
    return ConstFeature.conv(a)

  def dip_against(self, high: C, period: int) -> "FeatureGen":
    h = self._conv(high)
    gen = self._self() / h.moving_max(period) - 1
    return gen.as_name_of(
        f"dip_{self._self().feature_name}_against_max{period}_of_{h.feature_name}"
    )

  def dip_againsts(self, high: C, periods: list[int]) -> "Features":
    from declafe.feature_gen.Features import Features
    return Features([self.dip_against(high, p) for p in periods])

  def rip_against(self, low: C, period: int) -> "FeatureGen":
    l = self._conv(low)
    gen = self._self() / l.moving_min(period) - 1
    return gen.as_name_of(
        f"rip_{self._self().feature_name}_against_min{period}_of_{l.feature_name}"
    )

  def rip_againsts(self, low: C, periods: list[int]) -> "Features":
    from declafe.feature_gen.Features import Features
    return Features([self.rip_against(low, p) for p in periods])
