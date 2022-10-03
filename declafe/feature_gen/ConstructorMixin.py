from typing import TYPE_CHECKING, List, Type, Union

if TYPE_CHECKING:
  from declafe.feature_gen.Features import Features
  from ..feature_gen import FeatureGen


class ConstructorMixin:
  C = Union["FeatureGen", str]

  @classmethod
  def cond(cls, test: C, true: C, false: C) -> "FeatureGen":
    from declafe.feature_gen.tri.CondFeature import CondFeature
    return CondFeature(test_col=test, true_col=true, false_col=false)

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
  def aroon_osc(cls, high: C, low: C, period: int) -> "FeatureGen":
    from .binary.talib import AROONOSCFeature
    return AROONOSCFeature(high, low, period)

  @classmethod
  def aroon_oscs(cls, high: C, low: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.aroon_osc(high, low, period) for period in periods])

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

  @classmethod
  def stoch_slowd(cls,
                  high: C,
                  low: C,
                  close: C,
                  fastk_period: int,
                  slowk_period: int,
                  slowd_period: int,
                  slowd_matype: int = 0,
                  slowk_matype: int = 0) -> "FeatureGen":
    from .tri.talib.STOCHFeature import STOCHSlowdFeature
    return STOCHSlowdFeature(high=high,
                             low=low,
                             close=close,
                             fastk_period=fastk_period,
                             slowk_period=slowk_period,
                             slowd_period=slowd_period,
                             slowd_matype=slowd_matype,
                             slowk_matype=slowk_matype)

  @classmethod
  def stoch_slowk(cls,
                  high: C,
                  low: C,
                  close: C,
                  fastk_period: int,
                  slowk_period: int,
                  slowd_period: int,
                  slowd_matype: int = 0,
                  slowk_matype: int = 0) -> "FeatureGen":
    from .tri.talib.STOCHFeature import STOCHSlowkFeature
    return STOCHSlowkFeature(high=high,
                             low=low,
                             close=close,
                             fastk_period=fastk_period,
                             slowk_period=slowk_period,
                             slowd_period=slowd_period,
                             slowd_matype=slowd_matype,
                             slowk_matype=slowk_matype)

  @classmethod
  def stochf_fastk(cls,
                   high: C,
                   low: C,
                   close: C,
                   fastk_period: int,
                   fastd_period: int,
                   fastd_matype: int = 0) -> "FeatureGen":
    from .tri.talib.STOCHFFeature import STOCHFFastkFeature
    return STOCHFFastkFeature(high=high,
                              low=low,
                              close=close,
                              fastk_period=fastk_period,
                              fastd_period=fastd_period,
                              fastd_matype=fastd_matype)

  @classmethod
  def stochf_fastd(cls,
                   high: C,
                   low: C,
                   close: C,
                   fastk_period: int,
                   fastd_period: int,
                   fastd_matype: int = 0) -> "FeatureGen":
    from .tri.talib.STOCHFFeature import STOCHFFastdFeature
    return STOCHFFastdFeature(high=high,
                              low=low,
                              close=close,
                              fastk_period=fastk_period,
                              fastd_period=fastd_period,
                              fastd_matype=fastd_matype)

  @classmethod
  def ultosc(cls, high: C, low: C, close: C, timeperiod1: int, timeperiod2: int,
             timeperiod3: int) -> "FeatureGen":
    from .tri.talib.ULTOSCFeature import ULTOSCFeature
    return ULTOSCFeature(high=high,
                         low=low,
                         close=close,
                         timeperiod1=timeperiod1,
                         timeperiod2=timeperiod2,
                         timeperiod3=timeperiod3)

  @classmethod
  def willr(cls, high: C, low: C, close: C, timeperiod: int) -> "FeatureGen":
    from .tri.talib.WILLRFeature import WILLRFeature
    return WILLRFeature(high=high, low=low, close=close, timeperiod=timeperiod)

  @classmethod
  def willrs(cls, high: C, low: C, close: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.willr(high, low, close, period) for period in periods])

  @classmethod
  def ad(cls, high: C, low: C, close: C, volume: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.ADFeature import ADFeature
    return ADFeature(high=high, low=low, close=close, volume=volume)

  @classmethod
  def adosc(cls, high: C, low: C, close: C, volume: C, fastperiod: int,
            slowperiod: int) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.ADOSCFeature import ADOSCFeature
    return ADOSCFeature(high=high,
                        low=low,
                        close=close,
                        volume=volume,
                        fastperiod=fastperiod,
                        slowperiod=slowperiod)

  @classmethod
  def obv(cls, close: C, volume: C) -> "FeatureGen":
    from declafe.feature_gen.binary.talib.OBVFeature import OBVFeature
    return OBVFeature(close=close, volume=volume)

  @classmethod
  def atr(cls, high: C, low: C, close: C, timeperiod: int) -> "FeatureGen":
    from declafe.feature_gen.tri.talib.ATRFeature import ATRFeature
    return ATRFeature(high=high, low=low, close=close, timeperiod=timeperiod)

  @classmethod
  def atrs(cls, high: C, low: C, close: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.atr(high, low, close, period) for period in periods])

  @classmethod
  def natr(cls, high: C, low: C, close: C, timeperiod: int) -> "FeatureGen":
    from declafe.feature_gen.tri.talib.NATRFeature import NATRFeature
    return NATRFeature(high=high, low=low, close=close, timeperiod=timeperiod)

  @classmethod
  def natrs(cls, high: C, low: C, close: C, periods: List[int]) -> "Features":
    return cls._const_fs()(
        [cls.natr(high, low, close, period) for period in periods])

  @classmethod
  def trange(cls, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.tri.talib.TRANGEFeature import TRANGEFeature
    return TRANGEFeature(high=high, low=low, close=close)

  @classmethod
  def cdl2crows(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDL2CROWSFeature import CDL2CROWSFeature
    return CDL2CROWSFeature(opn=open, high=high, low=low, close=close)

  @classmethod
  def cdl3blackcrows(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDL3BLACKCROWSFeature import CDL3BLACKCROWSFeature
    return CDL3BLACKCROWSFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdl3inside(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDL3INSIDEFeature import CDL3INSIDEFeature
    return CDL3INSIDEFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdl3linestrike(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDL3LINESTRIKEFeature import CDL3LINESTRIKEFeature
    return CDL3LINESTRIKEFeature(open=open, high=high, low=low, close=close)

  @staticmethod
  def _const_fs() -> Type["Features"]:
    from declafe.feature_gen.Features import Features
    return Features
