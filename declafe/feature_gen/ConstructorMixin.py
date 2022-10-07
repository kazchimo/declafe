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

  @classmethod
  def cdl3outside(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDL3OUTSIDEFeature import CDL3OUTSIDEFeature
    return CDL3OUTSIDEFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdl3starsinsouth(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDL3STARSINSOUTHFeature import CDL3STARSINSOUTHFeature
    return CDL3STARSINSOUTHFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdl3whitesoldiers(cls, open: C, high: C, low: C,
                        close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDL3WHITESOLDIERSFeature import CDL3WHITESOLDIERSFeature
    return CDL3WHITESOLDIERSFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlabandonedbaby(cls, open: C, high: C, low: C, close: C,
                       penetration: float) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLABANDONEDBABYFeature import CDLABANDONEDBABYFeature
    return CDLABANDONEDBABYFeature(open=open,
                                   high=high,
                                   low=low,
                                   close=close,
                                   penetration=penetration)

  @classmethod
  def cdladvanceblock(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLADVANCEBLOCKFeature import CDLADVANCEBLOCKFeature
    return CDLADVANCEBLOCKFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlbelthold(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLBELTHOLDFeature import CDLBELTHOLDFeature
    return CDLBELTHOLDFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlbreakaway(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLBREAKAWAYFeature import CDLBREAKAWAYFeature
    return CDLBREAKAWAYFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlclosingmarubozu(cls, open: C, high: C, low: C,
                         close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLCLOSINGMARUBOZUFeature import CDLCLOSINGMARUBOZUFeature
    return CDLCLOSINGMARUBOZUFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlconcealbabyswall(cls, open: C, high: C, low: C,
                          close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLCONCEALBABYSWALLFeature import CDLCONCEALBABYSWALLFeature
    return CDLCONCEALBABYSWALLFeature(open=open,
                                      high=high,
                                      low=low,
                                      close=close)

  @classmethod
  def cdlcounterattack(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLCOUNTERATTACKFeature import CDLCOUNTERATTACKFeature
    return CDLCOUNTERATTACKFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdldarkcloudcover(cls, open: C, high: C, low: C, close: C,
                        penetration: float) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLDARKCLOUDCOVERFeature import CDLDARKCLOUDCOVERFeature
    return CDLDARKCLOUDCOVERFeature(open=open,
                                    high=high,
                                    low=low,
                                    close=close,
                                    penetration=penetration)

  @classmethod
  def cdldoji(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLDOJIFeature import CDLDOJIFeature
    return CDLDOJIFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdldojistar(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLDOJISTARFeature import CDLDOJISTARFeature
    return CDLDOJISTARFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdldragonflydoji(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLDRAGONFLYDOJIFeature import CDLDRAGONFLYDOJIFeature
    return CDLDRAGONFLYDOJIFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlengulfing(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLENGULFINGFeature import CDLENGULFINGFeature
    return CDLENGULFINGFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdleveningdojistar(cls, open: C, high: C, low: C, close: C,
                         penetration: float) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLEVENINGDOJISTARFeature import CDLEVENINGDOJISTARFeature
    return CDLEVENINGDOJISTARFeature(open=open,
                                     high=high,
                                     low=low,
                                     close=close,
                                     penetration=penetration)

  @classmethod
  def cdleveningstar(cls, open: C, high: C, low: C, close: C,
                     penetration: float) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLEVENINGSTARFeature import CDLEVENINGSTARFeature
    return CDLEVENINGSTARFeature(open=open,
                                 high=high,
                                 low=low,
                                 close=close,
                                 penetration=penetration)

  @classmethod
  def cdlgapsidesidewhite(cls, open: C, high: C, low: C,
                          close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLGAPSIDESIDEWHITEFeature import CDLGAPSIDESIDEWHITEFeature
    return CDLGAPSIDESIDEWHITEFeature(open=open,
                                      high=high,
                                      low=low,
                                      close=close)

  @classmethod
  def cdlgravestonedoji(cls, open: C, high: C, low: C,
                        close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLGRAVESTONEDOJIFeature import CDLGRAVESTONEDOJIFeature
    return CDLGRAVESTONEDOJIFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlhammer(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLHAMMERFeature import CDLHAMMERFeature
    return CDLHAMMERFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlhangingman(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLHANGINGMANFeature import CDLHANGINGMANFeature
    return CDLHANGINGMANFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlharami(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLHARAMIFeature import CDLHARAMIFeature
    return CDLHARAMIFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlharamicross(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLHARAMICROSSFeature import CDLHARAMICROSSFeature
    return CDLHARAMICROSSFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlhighwave(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLHIGHWAVEFeature import CDLHIGHWAVEFeature
    return CDLHIGHWAVEFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlhikkake(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLHIKKAKEFeature import CDLHIKKAKEFeature
    return CDLHIKKAKEFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlhikkakemod(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLHIKKAKEMODFeature import CDLHIKKAKEMODFeature
    return CDLHIKKAKEMODFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlhomingpigeon(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLHOMINGPIGEONFeature import CDLHOMINGPIGEONFeature
    return CDLHOMINGPIGEONFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlidentical3crows(cls, open: C, high: C, low: C,
                         close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLIDENTICAL3CROWSFeature import CDLIDENTICAL3CROWSFeature
    return CDLIDENTICAL3CROWSFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlinneck(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLINNECKFeature import CDLINNECKFeature
    return CDLINNECKFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlinvertedhammer(cls, open: C, high: C, low: C,
                        close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLINVERTEDHAMMERFeature import CDLINVERTEDHAMMERFeature
    return CDLINVERTEDHAMMERFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlkicking(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLKICKINGFeature import CDLKICKINGFeature
    return CDLKICKINGFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlkickingbylength(cls, open: C, high: C, low: C,
                         close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLKICKINGBYLENGTHFeature import CDLKICKINGBYLENGTHFeature
    return CDLKICKINGBYLENGTHFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlladderbottom(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLLADDERBOTTOMFeature import CDLLADDERBOTTOMFeature
    return CDLLADDERBOTTOMFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdllongleggeddoji(cls, open: C, high: C, low: C,
                        close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLLONGLEGGEDDOJIFeature import CDLLONGLEGGEDDOJIFeature
    return CDLLONGLEGGEDDOJIFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdllongline(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLLONGLINEFeature import CDLLONGLINEFeature
    return CDLLONGLINEFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlmarubozu(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLMARUBOZUFeature import CDLMARUBOZUFeature
    return CDLMARUBOZUFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlmatchinglow(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLMATCHINGLOWFeature import CDLMATCHINGLOWFeature
    return CDLMATCHINGLOWFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlmathold(cls,
                 open: C,
                 high: C,
                 low: C,
                 close: C,
                 penetration: float = 0) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLMATHOLDFeature import CDLMATHOLDFeature
    return CDLMATHOLDFeature(open=open,
                             high=high,
                             low=low,
                             close=close,
                             penetration=penetration)

  @classmethod
  def cdlmorningdojistar(cls,
                         open: C,
                         high: C,
                         low: C,
                         close: C,
                         penetration: float = 0) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLMORNINGDOJISTARFeature import CDLMORNINGDOJISTARFeature
    return CDLMORNINGDOJISTARFeature(open=open,
                                     high=high,
                                     low=low,
                                     close=close,
                                     penetration=penetration)

  @classmethod
  def cdlmorningstar(cls,
                     open: C,
                     high: C,
                     low: C,
                     close: C,
                     penetration: float = 0) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLMORNINGSTARFeature import CDLMORNINGSTARFeature
    return CDLMORNINGSTARFeature(open=open,
                                 high=high,
                                 low=low,
                                 close=close,
                                 penetration=penetration)

  @classmethod
  def cdlonneck(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLONNECKFeature import CDLONNECKFeature
    return CDLONNECKFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlpiercing(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLPIERCINGFeature import CDLPIERCINGFeature
    return CDLPIERCINGFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlrickshawman(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLRICKSHAWMANFeature import CDLRICKSHAWMANFeature
    return CDLRICKSHAWMANFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlrisefall3methods(cls, open: C, high: C, low: C,
                          close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLRISEFALL3METHODSFeature import CDLRISEFALL3METHODSFeature
    return CDLRISEFALL3METHODSFeature(open=open,
                                      high=high,
                                      low=low,
                                      close=close)

  @classmethod
  def cdlseparatinglines(cls, open: C, high: C, low: C,
                         close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLSEPARATINGLINESFeature import CDLSEPARATINGLINESFeature
    return CDLSEPARATINGLINESFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlshootingstar(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLSHOOTINGSTARFeature import CDLSHOOTINGSTARFeature
    return CDLSHOOTINGSTARFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlshortline(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLSHORTLINEFeature import CDLSHORTLINEFeature
    return CDLSHORTLINEFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlspinningtop(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLSPINNINGTOPFeature import CDLSPINNINGTOPFeature
    return CDLSPINNINGTOPFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlstalledpattern(cls, open: C, high: C, low: C,
                        close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLSTALLEDPATTERNFeature import CDLSTALLEDPATTERNFeature
    return CDLSTALLEDPATTERNFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlsticksandwich(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLSTICKSANDWICHFeature import CDLSTICKSANDWICHFeature
    return CDLSTICKSANDWICHFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdltakuri(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLTAKURIFeature import CDLTAKURIFeature
    return CDLTAKURIFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdltasukigap(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLTASUKIGAPFeature import CDLTASUKIGAPFeature
    return CDLTASUKIGAPFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlthrusting(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLTHRUSTINGFeature import CDLTHRUSTINGFeature
    return CDLTHRUSTINGFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdltristar(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLTRISTARFeature import CDLTRISTARFeature
    return CDLTRISTARFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlunique3river(cls, open: C, high: C, low: C, close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLUNIQUE3RIVERFeature import CDLUNIQUE3RIVERFeature
    return CDLUNIQUE3RIVERFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlupsidegap2crows(cls, open: C, high: C, low: C,
                         close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLUPSIDEGAP2CROWSFeature import CDLUPSIDEGAP2CROWSFeature
    return CDLUPSIDEGAP2CROWSFeature(open=open, high=high, low=low, close=close)

  @classmethod
  def cdlxsidegap3methods(cls, open: C, high: C, low: C,
                          close: C) -> "FeatureGen":
    from declafe.feature_gen.quadri.talib.CDLXSIDEGAP3METHODSFeature import CDLXSIDEGAP3METHODSFeature
    return CDLXSIDEGAP3METHODSFeature(open=open,
                                      high=high,
                                      low=low,
                                      close=close)

  @staticmethod
  def _const_fs() -> Type["Features"]:
    from declafe.feature_gen.Features import Features
    return Features
