from abc import ABC
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
  from lib.features import FeatureGen

class StaticMixin(ABC):
  @staticmethod
  def sar(high: str, low: str) -> "FeatureGen":
    from lib.features.binary import SARFeature
    return SARFeature(high, low)

  @staticmethod
  def sarext(high: str, low: str) -> "FeatureGen":
    from lib.features.binary import SAREXTFeature
    return SAREXTFeature(high, low)

  @classmethod
  def adxes(cls, high: str, low: str, close: str, periods: List[int]) -> List["FeatureGen"]:
    return [cls.adx(high, low, close, period) for period in periods]

  @staticmethod
  def adx(high: str, low: str, close: str, period: int) -> "FeatureGen":
    from lib.features.tri.ADXFeature import ADXFeature
    return ADXFeature(high, low, close, period)

  @classmethod
  def adxrs(cls, high: str, low: str, close: str, periods: List[int]) -> List["FeatureGen"]:
    return [cls.adx(high, low, close, period) for period in periods]

  @staticmethod
  def adxr(high: str, low: str, close: str, period: int) -> "FeatureGen":
    from lib.features.tri import ADXRFeature
    return ADXRFeature(high, low, close, period)

  @staticmethod
  def aroon_up(high: str, low: str, period: int) -> "FeatureGen":
    from lib.features.binary import AROONUpFeature
    return AROONUpFeature(high, low, period)

  @classmethod
  def aroon_ups(cls, high: str, low: str, periods: List[int]) -> List["FeatureGen"]:
    return [cls.aroon_up(high, low, period) for period in periods]

  @staticmethod
  def aroon_down(high: str, low: str, period: int) -> "FeatureGen":
    from lib.features.binary import AROONDownFeature
    return AROONDownFeature(high, low, period)

  @classmethod
  def aroon_downs(cls, high: str, low: str, periods: List[int]) -> List["FeatureGen"]:
    return [cls.aroon_down(high, low, period) for period in periods]

  @staticmethod
  def arron_osc(high: str, low: str, period: int) -> "FeatureGen":
    from lib.features.binary import AROONOSCFeature
    return AROONOSCFeature(high, low, period)

  @classmethod
  def arron_oscs(cls, high: str, low: str, periods: List[int]) -> List["FeatureGen"]:
    return [cls.arron_osc(high, low, period) for period in periods]

  @staticmethod
  def bop(open_col: str = "open", high: str = "high", low: str = "low", close: str = "close") -> "FeatureGen":
    from lib.features.quadri import BOPFeature
    return BOPFeature(open_col, high, low, close)
