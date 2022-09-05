from typing import TYPE_CHECKING, List, Type

if TYPE_CHECKING:
  from declafe.feature_gen.Features import Features
  from ..feature_gen import FeatureGen


class ConstructorMixin:

  @staticmethod
  def sar(high: str, low: str) -> "FeatureGen":
    from declafe.feature_gen.binary import SARFeature
    return SARFeature(high, low)

  @staticmethod
  def sarext(high: str, low: str) -> "FeatureGen":
    from declafe.feature_gen.binary import SAREXTFeature
    return SAREXTFeature(high, low)

  @staticmethod
  def midprice(high: str, low: str) -> "FeatureGen":
    from declafe.feature_gen.binary import MIDPRICEFeature
    return MIDPRICEFeature(high, low)

  @classmethod
  def adxes(cls, high: str, low: str, close: str,
            periods: List[int]) -> "Features":
    return cls._const_fs()([cls.adx(high, low, close, period) for period in periods])

  @staticmethod
  def adx(high: str, low: str, close: str, period: int) -> "FeatureGen":
    from declafe.feature_gen.tri.talib.ADXFeature import ADXFeature
    return ADXFeature(high, low, close, period)

  @classmethod
  def adxrs(cls, high: str, low: str, close: str,
            periods: List[int]) -> "Features":
    return cls._const_fs()([cls.adx(high, low, close, period) for period in periods])

  @staticmethod
  def adxr(high: str, low: str, close: str, period: int) -> "FeatureGen":
    from .tri.talib.ADXRFeature import ADXRFeature
    return ADXRFeature(high, low, close, period)

  @classmethod
  def ccis(cls, high: str, low: str, close: str,
            periods: List[int]) -> "Features":
    return cls._const_fs()([cls.cci(high, low, close, period) for period in periods])

  @staticmethod
  def cci(high: str, low: str, close: str, period: int) -> "FeatureGen":
    from .tri.talib.CCIFeature import CCIFeature
    return CCIFeature(high, low, close, period)

  @staticmethod
  def aroon_up(high: str, low: str, period: int) -> "FeatureGen":
    from .binary.talib import AROONUpFeature
    return AROONUpFeature(high, low, period)

  @classmethod
  def aroon_ups(cls, high: str, low: str, periods: List[int]) -> "Features":
    return cls._const_fs()([cls.aroon_up(high, low, period) for period in periods])

  @staticmethod
  def aroon_down(high: str, low: str, period: int) -> "FeatureGen":
    from .binary.talib import AROONDownFeature
    return AROONDownFeature(high, low, period)

  @classmethod
  def aroon_downs(cls, high: str, low: str, periods: List[int]) -> "Features":
    return cls._const_fs()([cls.aroon_down(high, low, period) for period in periods])

  @staticmethod
  def arron_osc(high: str, low: str, period: int) -> "FeatureGen":
    from .binary.talib import AROONOSCFeature
    return AROONOSCFeature(high, low, period)

  @classmethod
  def arron_oscs(cls, high: str, low: str, periods: List[int]) -> "Features":
    return cls._const_fs()([cls.arron_osc(high, low, period) for period in periods])

  @staticmethod
  def bop(open_col: str = "open",
          high: str = "high",
          low: str = "low",
          close: str = "close") -> "FeatureGen":
    from .quadri.talib import BOPFeature
    return BOPFeature(open_col, high, low, close)

  @staticmethod
  def _const_fs() -> Type["Features"]:
    from declafe.feature_gen.Features import Features
    return Features
