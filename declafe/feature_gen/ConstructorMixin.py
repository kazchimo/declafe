from typing import TYPE_CHECKING, List, Type, Union

if TYPE_CHECKING:
  from declafe.feature_gen.Features import Features
  from ..feature_gen import FeatureGen


class ConstructorMixin:
  C = Union["FeatureGen", str]

  @classmethod
  def sar(cls, high: C, low: C) -> "FeatureGen":
    from declafe.feature_gen.binary import SARFeature
    return SARFeature(high, low)

  @classmethod
  def sarext(cls, high: C, low: C) -> "FeatureGen":
    from declafe.feature_gen.binary import SAREXTFeature
    return SAREXTFeature(high, low)

  @classmethod
  def midprice(cls, high: C, low: C, period: int) -> "FeatureGen":
    from declafe.feature_gen.binary import MIDPRICEFeature
    return MIDPRICEFeature(high, low, period)

  @classmethod
  def midprices(cls, high: C, low: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.midprice(high, low, period) for period in periods])

  @classmethod
  def adxes(cls, high: C, low: C, close: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.adx(high, low, close, period) for period in periods])

  @classmethod
  def adx(cls, high: C, low: C, close: C, period: int) -> "FeatureGen":
    from declafe.feature_gen.tri.talib.ADXFeature import ADXFeature
    return ADXFeature(high, low, close, period)

  @classmethod
  def adxrs(cls, high: C, low: C, close: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.adxr(high, low, close, period) for period in periods])

  @classmethod
  def adxr(cls, high: C, low: C, close: C, period: int) -> "FeatureGen":
    from .tri.talib.ADXRFeature import ADXRFeature
    return ADXRFeature(high, low, close, period)

  @classmethod
  def ccis(cls, high: C, low: C, close: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.cci(high, low, close, period) for period in periods])

  @classmethod
  def cci(cls, high: C, low: C, close: C, period: int) -> "FeatureGen":
    from .tri.talib.CCIFeature import CCIFeature
    return CCIFeature(high, low, close, period)

  @classmethod
  def aroon_up(cls, high: C, low: C, period: int) -> "FeatureGen":
    from .binary.talib import AROONUpFeature
    return AROONUpFeature(high, low, period)

  @classmethod
  def aroon_ups(cls, high: C, low: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.aroon_up(high, low, period) for period in periods])

  @classmethod
  def aroon_down(cls, high: C, low: C, period: int) -> "FeatureGen":
    from .binary.talib import AROONDownFeature
    return AROONDownFeature(high, low, period)

  @classmethod
  def aroon_downs(cls, high: C, low: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.aroon_down(high, low, period) for period in periods])

  @classmethod
  def arron_osc(cls, high: C, low: C, period: int) -> "FeatureGen":
    from .binary.talib import AROONOSCFeature
    return AROONOSCFeature(high, low, period)

  @classmethod
  def arron_oscs(cls, high: C, low: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.arron_osc(high, low, period) for period in periods])

  @classmethod
  def bop(cls,
          open_col: C = "open",
          high: C = "high",
          low: C = "low",
          close: C = "close") -> "FeatureGen":
    from .quadri.talib import BOPFeature
    return BOPFeature(open_col, high, low, close)

  @classmethod
  def dx(cls, high: C, low: C, close: C, period: int) -> "FeatureGen":
    from .tri.talib.DXFeature import DXFeature
    return DXFeature(high, low, close, period)

  @classmethod
  def dxes(cls, high: C, low: C, close: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.dx(high, low, close, period) for period in periods])

  @classmethod
  def mfi(cls, high: C, low: C, close: C, volume: C,
          period: int) -> "FeatureGen":
    from .quadri.talib.MFIFeature import MFIFeature
    return MFIFeature(high, low, close, volume, period)

  @classmethod
  def mfis(cls, high: C, low: C, close: C, volume: C,
           periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.mfi(high, low, close, volume, period) for period in periods])

  @classmethod
  def minus_di(cls, high: C, low: C, close: C, period: int) -> "FeatureGen":
    from .tri.talib.MinusDIFeature import MinusDIFeature
    return MinusDIFeature(high, low, close, period)

  @classmethod
  def minus_dis(cls, high: C, low: C, close: C,
                periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.minus_di(high, low, close, period) for period in periods])

  @classmethod
  def minus_dm(cls, high: C, low: C, period: int) -> "FeatureGen":
    from .binary.talib.MinusDMFeature import MinusDMFeature
    return MinusDMFeature(high, low, period)

  @classmethod
  def minus_dms(cls, high: C, low: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.minus_dm(high, low, period) for period in periods])

  @classmethod
  def plus_di(cls, high: C, low: C, close: C, period: int) -> "FeatureGen":
    from .tri.talib.PlusDIFeature import PlusDIFeature
    return PlusDIFeature(high, low, close, period)

  @classmethod
  def plus_dis(cls, high: C, low: C, close: C,
               periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.plus_di(high, low, close, period) for period in periods])

  @classmethod
  def plus_dm(cls, high: C, low: C, period: int) -> "FeatureGen":
    from .binary.talib.PlusDMFeature import PlusDMFeature
    return PlusDMFeature(high, low, period)

  @classmethod
  def plus_dms(cls, high: C, low: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.plus_dm(high, low, period) for period in periods])

  @staticmethod
  def _const_fs() -> Type["Features"]:
    from declafe.feature_gen.Features import Features
    return Features
