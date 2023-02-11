from declafe.pl.feature_gen.types import ColLike
from declafe.pl.feature_gen.feature_gen import FeatureGen


# noinspection PyMethodMayBeStatic,SpellCheckingInspection
class TalibConstructor:

  def __init__(self):
    super().__init__()

  def dx(self, high: ColLike, low: ColLike, close: ColLike,
         timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.dx_feature import DXFeature
    return DXFeature(high, low, close, timeperiod)

  def trange(self, high: ColLike, low: ColLike, close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.trange_feature import TRANGEFeature
    return TRANGEFeature(high, low, close)

  def natr(self,
           high: ColLike,
           low: ColLike,
           close: ColLike,
           timeperiod: int = 14) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.natr_feature import NATRFeature
    return NATRFeature(high, low, close, timeperiod)

  def willr(self,
            high: ColLike,
            low: ColLike,
            close: ColLike,
            timeperiod: int = 14) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.willr_feature import WILLRFeature
    return WILLRFeature(high, low, close, timeperiod)

  def adxr(self, high: ColLike, low: ColLike, close: ColLike,
           timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.adxr_feature import ADXRFeature
    return ADXRFeature(high, low, close, timeperiod)

  def stoch_0(self, high: ColLike, low: ColLike, close: ColLike,
              fastk_period: int, slowk_period: int, slowk_matype: int,
              slowd_period: int, slowd_matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.stoch_feature import STOCH_0Feature
    return STOCH_0Feature(high, low, close, fastk_period, slowk_period,
                          slowk_matype, slowd_period, slowd_matype)

  def stoch_fastk(self, high: ColLike, low: ColLike, close: ColLike,
                  fastk_period: int, slowk_period: int, slowk_matype: int,
                  slowd_period: int, slowd_matype: int) -> "FeatureGen":
    return self.stoch_0(high, low, close, fastk_period, slowk_period,
                        slowk_matype, slowd_period, slowd_matype)

  def stoch_1(self, high: ColLike, low: ColLike, close: ColLike,
              fastk_period: int, slowk_period: int, slowk_matype: int,
              slowd_period: int, slowd_matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.stoch_feature import STOCH_1Feature
    return STOCH_1Feature(high, low, close, fastk_period, slowk_period,
                          slowk_matype, slowd_period, slowd_matype)

  def stoch_fastd(self, high: ColLike, low: ColLike, close: ColLike,
                  fastk_period: int, slowk_period: int, slowk_matype: int,
                  slowd_period: int, slowd_matype: int) -> "FeatureGen":
    return self.stoch_1(high, low, close, fastk_period, slowk_period,
                        slowk_matype, slowd_period, slowd_matype)

  def minus_di(self, high: ColLike, low: ColLike, close: ColLike,
               timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.minus_di_feature import MINUS_DIFeature
    return MINUS_DIFeature(high, low, close, timeperiod)

  def stochf_0(self, high: ColLike, low: ColLike, close: ColLike,
               fastk_period: int, fastd_period: int,
               fastd_matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.stochf_feature import STOCHF_0Feature
    return STOCHF_0Feature(high, low, close, fastk_period, fastd_period,
                           fastd_matype)

  def stochf_fastk(self, high: ColLike, low: ColLike, close: ColLike,
                   fastk_period: int, fastd_period: int,
                   fastd_matype: int) -> "FeatureGen":
    return self.stochf_0(high, low, close, fastk_period, fastd_period,
                         fastd_matype)

  def stochf_1(self, high: ColLike, low: ColLike, close: ColLike,
               fastk_period: int, fastd_period: int,
               fastd_matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.stochf_feature import STOCHF_1Feature
    return STOCHF_1Feature(high, low, close, fastk_period, fastd_period,
                           fastd_matype)

  def stochf_fastd(self, high: ColLike, low: ColLike, close: ColLike,
                   fastk_period: int, fastd_period: int,
                   fastd_matype: int) -> "FeatureGen":
    return self.stochf_1(high, low, close, fastk_period, fastd_period,
                         fastd_matype)

  def cci(self, high: ColLike, low: ColLike, close: ColLike,
          timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.cci_feature import CCIFeature
    return CCIFeature(high, low, close, timeperiod)

  def ultosc(self,
             high: ColLike,
             low: ColLike,
             close: ColLike,
             timeperiod1: int = 7,
             timeperiod2: int = 14,
             timeperiod3: int = 28) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.ultosc_feature import ULTOSCFeature
    return ULTOSCFeature(high, low, close, timeperiod1, timeperiod2,
                         timeperiod3)

  def atr(self,
          high: ColLike,
          low: ColLike,
          close: ColLike,
          timeperiod: int = 14) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.atr_feature import ATRFeature
    return ATRFeature(high, low, close, timeperiod)

  def plus_di(self,
              high: ColLike,
              low: ColLike,
              close: ColLike,
              timeperiod: int = 14) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.plus_di_feature import PLUS_DIFeature
    return PLUS_DIFeature(high, low, close, timeperiod)

  def adx(self, high: ColLike, low: ColLike, close: ColLike,
          timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.tri.talib.adx_feature import ADXFeature
    return ADXFeature(high, low, close, timeperiod)

  def cdlbreakaway(self, open: ColLike, high: ColLike, low: ColLike,
                   close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlbreakaway_feature import CDLBREAKAWAYFeature
    return CDLBREAKAWAYFeature(open, high, low, close)

  def cdlrickshawman(self, open: ColLike, high: ColLike, low: ColLike,
                     close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlrickshawman_feature import CDLRICKSHAWMANFeature
    return CDLRICKSHAWMANFeature(open, high, low, close)

  def cdlmorningdojistar(self,
                         open: ColLike,
                         high: ColLike,
                         low: ColLike,
                         close: ColLike,
                         penetration: float = 0) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlmorningdojistar_feature import CDLMORNINGDOJISTARFeature
    return CDLMORNINGDOJISTARFeature(open, high, low, close, penetration)

  def cdl3starsinsouth(self, open: ColLike, high: ColLike, low: ColLike,
                       close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdl3starsinsouth_feature import CDL3STARSINSOUTHFeature
    return CDL3STARSINSOUTHFeature(open, high, low, close)

  def cdlladderbottom(self, open: ColLike, high: ColLike, low: ColLike,
                      close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlladderbottom_feature import CDLLADDERBOTTOMFeature
    return CDLLADDERBOTTOMFeature(open, high, low, close)

  def cdldarkcloudcover(self, open: ColLike, high: ColLike, low: ColLike,
                        close: ColLike, penetration: float) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdldarkcloudcover_feature import CDLDARKCLOUDCOVERFeature
    return CDLDARKCLOUDCOVERFeature(open, high, low, close, penetration)

  def cdlpiercing(self, open: ColLike, high: ColLike, low: ColLike,
                  close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlpiercing_feature import CDLPIERCINGFeature
    return CDLPIERCINGFeature(open, high, low, close)

  def cdlstalledpattern(self, open: ColLike, high: ColLike, low: ColLike,
                        close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlstalledpattern_feature import CDLSTALLEDPATTERNFeature
    return CDLSTALLEDPATTERNFeature(open, high, low, close)

  def cdlinneck(self, open: ColLike, high: ColLike, low: ColLike,
                close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlinneck_feature import CDLINNECKFeature
    return CDLINNECKFeature(open, high, low, close)

  def cdlgravestonedoji(self, open: ColLike, high: ColLike, low: ColLike,
                        close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlgravestonedoji_feature import CDLGRAVESTONEDOJIFeature
    return CDLGRAVESTONEDOJIFeature(open, high, low, close)

  def cdl3linestrike(self, open: ColLike, high: ColLike, low: ColLike,
                     close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdl3linestrike_feature import CDL3LINESTRIKEFeature
    return CDL3LINESTRIKEFeature(open, high, low, close)

  def cdlabandonedbaby(self, open: ColLike, high: ColLike, low: ColLike,
                       close: ColLike, penetration: float) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlabandonedbaby_feature import CDLABANDONEDBABYFeature
    return CDLABANDONEDBABYFeature(open, high, low, close, penetration)

  def cdl2crows(self, open: ColLike, high: ColLike, low: ColLike,
                close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdl2crows_feature import CDL2CROWSFeature
    return CDL2CROWSFeature(open, high, low, close)

  def cdlunique3river(self, open: ColLike, high: ColLike, low: ColLike,
                      close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlunique3river_feature import CDLUNIQUE3RIVERFeature
    return CDLUNIQUE3RIVERFeature(open, high, low, close)

  def cdl3blackcrows(self, open: ColLike, high: ColLike, low: ColLike,
                     close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdl3blackcrows_feature import CDL3BLACKCROWSFeature
    return CDL3BLACKCROWSFeature(open, high, low, close)

  def mfi(self, high: ColLike, low: ColLike, close: ColLike, volume: ColLike,
          timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.mfi_feature import MFIFeature
    return MFIFeature(high, low, close, volume, timeperiod)

  def cdlhomingpigeon(self, open: ColLike, high: ColLike, low: ColLike,
                      close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlhomingpigeon_feature import CDLHOMINGPIGEONFeature
    return CDLHOMINGPIGEONFeature(open, high, low, close)

  def adosc(self,
            high: ColLike,
            low: ColLike,
            close: ColLike,
            volume: ColLike,
            fastperiod: int = 3,
            slowperiod: int = 10) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.adosc_feature import ADOSCFeature
    return ADOSCFeature(high, low, close, volume, fastperiod, slowperiod)

  def cdlcounterattack(self, open: ColLike, high: ColLike, low: ColLike,
                       close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlcounterattack_feature import CDLCOUNTERATTACKFeature
    return CDLCOUNTERATTACKFeature(open, high, low, close)

  def cdlidentical3crows(self, open: ColLike, high: ColLike, low: ColLike,
                         close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlidentical3crows_feature import CDLIDENTICAL3CROWSFeature
    return CDLIDENTICAL3CROWSFeature(open, high, low, close)

  def cdlmorningstar(self,
                     open: ColLike,
                     high: ColLike,
                     low: ColLike,
                     close: ColLike,
                     penetration: float = 0) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlmorningstar_feature import CDLMORNINGSTARFeature
    return CDLMORNINGSTARFeature(open, high, low, close, penetration)

  def cdllongleggeddoji(self, open: ColLike, high: ColLike, low: ColLike,
                        close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdllongleggeddoji_feature import CDLLONGLEGGEDDOJIFeature
    return CDLLONGLEGGEDDOJIFeature(open, high, low, close)

  def cdlseparatinglines(self, open: ColLike, high: ColLike, low: ColLike,
                         close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlseparatinglines_feature import CDLSEPARATINGLINESFeature
    return CDLSEPARATINGLINESFeature(open, high, low, close)

  def cdlspinningtop(self, open: ColLike, high: ColLike, low: ColLike,
                     close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlspinningtop_feature import CDLSPINNINGTOPFeature
    return CDLSPINNINGTOPFeature(open, high, low, close)

  def cdllongline(self, open: ColLike, high: ColLike, low: ColLike,
                  close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdllongline_feature import CDLLONGLINEFeature
    return CDLLONGLINEFeature(open, high, low, close)

  def cdlinvertedhammer(self, open: ColLike, high: ColLike, low: ColLike,
                        close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlinvertedhammer_feature import CDLINVERTEDHAMMERFeature
    return CDLINVERTEDHAMMERFeature(open, high, low, close)

  def cdlxsidegap3methods(self, open: ColLike, high: ColLike, low: ColLike,
                          close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlxsidegap3methods_feature import CDLXSIDEGAP3METHODSFeature
    return CDLXSIDEGAP3METHODSFeature(open, high, low, close)

  def cdlengulfing(self, open: ColLike, high: ColLike, low: ColLike,
                   close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlengulfing_feature import CDLENGULFINGFeature
    return CDLENGULFINGFeature(open, high, low, close)

  def cdlhikkakemod(self, open: ColLike, high: ColLike, low: ColLike,
                    close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlhikkakemod_feature import CDLHIKKAKEMODFeature
    return CDLHIKKAKEMODFeature(open, high, low, close)

  def cdlharami(self, open: ColLike, high: ColLike, low: ColLike,
                close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlharami_feature import CDLHARAMIFeature
    return CDLHARAMIFeature(open, high, low, close)

  def cdladvanceblock(self, open: ColLike, high: ColLike, low: ColLike,
                      close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdladvanceblock_feature import CDLADVANCEBLOCKFeature
    return CDLADVANCEBLOCKFeature(open, high, low, close)

  def cdltasukigap(self, open: ColLike, high: ColLike, low: ColLike,
                   close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdltasukigap_feature import CDLTASUKIGAPFeature
    return CDLTASUKIGAPFeature(open, high, low, close)

  def cdlonneck(self, open: ColLike, high: ColLike, low: ColLike,
                close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlonneck_feature import CDLONNECKFeature
    return CDLONNECKFeature(open, high, low, close)

  def cdldojistar(self, open: ColLike, high: ColLike, low: ColLike,
                  close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdldojistar_feature import CDLDOJISTARFeature
    return CDLDOJISTARFeature(open, high, low, close)

  def ad(self, high: ColLike, low: ColLike, close: ColLike,
         volume: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.ad_feature import ADFeature
    return ADFeature(high, low, close, volume)

  def cdlsticksandwich(self, open: ColLike, high: ColLike, low: ColLike,
                       close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlsticksandwich_feature import CDLSTICKSANDWICHFeature
    return CDLSTICKSANDWICHFeature(open, high, low, close)

  def cdlshortline(self, open: ColLike, high: ColLike, low: ColLike,
                   close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlshortline_feature import CDLSHORTLINEFeature
    return CDLSHORTLINEFeature(open, high, low, close)

  def cdl3outside(self, open: ColLike, high: ColLike, low: ColLike,
                  close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdl3outside_feature import CDL3OUTSIDEFeature
    return CDL3OUTSIDEFeature(open, high, low, close)

  def cdlkicking(self, open: ColLike, high: ColLike, low: ColLike,
                 close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlkicking_feature import CDLKICKINGFeature
    return CDLKICKINGFeature(open, high, low, close)

  def cdldragonflydoji(self, open: ColLike, high: ColLike, low: ColLike,
                       close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdldragonflydoji_feature import CDLDRAGONFLYDOJIFeature
    return CDLDRAGONFLYDOJIFeature(open, high, low, close)

  def cdlhighwave(self, open: ColLike, high: ColLike, low: ColLike,
                  close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlhighwave_feature import CDLHIGHWAVEFeature
    return CDLHIGHWAVEFeature(open, high, low, close)

  def cdlmathold(self,
                 open: ColLike,
                 high: ColLike,
                 low: ColLike,
                 close: ColLike,
                 penetration: float = 0) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlmathold_feature import CDLMATHOLDFeature
    return CDLMATHOLDFeature(open, high, low, close, penetration)

  def cdlhikkake(self, open: ColLike, high: ColLike, low: ColLike,
                 close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlhikkake_feature import CDLHIKKAKEFeature
    return CDLHIKKAKEFeature(open, high, low, close)

  def cdldoji(self, open: ColLike, high: ColLike, low: ColLike,
              close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdldoji_feature import CDLDOJIFeature
    return CDLDOJIFeature(open, high, low, close)

  def cdleveningstar(self, open: ColLike, high: ColLike, low: ColLike,
                     close: ColLike, penetration: float) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdleveningstar_feature import CDLEVENINGSTARFeature
    return CDLEVENINGSTARFeature(open, high, low, close, penetration)

  def cdlgapsidesidewhite(self, open: ColLike, high: ColLike, low: ColLike,
                          close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlgapsidesidewhite_feature import CDLGAPSIDESIDEWHITEFeature
    return CDLGAPSIDESIDEWHITEFeature(open, high, low, close)

  def cdltristar(self, open: ColLike, high: ColLike, low: ColLike,
                 close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdltristar_feature import CDLTRISTARFeature
    return CDLTRISTARFeature(open, high, low, close)

  def cdlthrusting(self, open: ColLike, high: ColLike, low: ColLike,
                   close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlthrusting_feature import CDLTHRUSTINGFeature
    return CDLTHRUSTINGFeature(open, high, low, close)

  def cdlshootingstar(self, open: ColLike, high: ColLike, low: ColLike,
                      close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlshootingstar_feature import CDLSHOOTINGSTARFeature
    return CDLSHOOTINGSTARFeature(open, high, low, close)

  def cdlbelthold(self, open: ColLike, high: ColLike, low: ColLike,
                  close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlbelthold_feature import CDLBELTHOLDFeature
    return CDLBELTHOLDFeature(open, high, low, close)

  def bop(self, open: ColLike, high: ColLike, low: ColLike,
          close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.bop_feature import BOPFeature
    return BOPFeature(open, high, low, close)

  def cdlhammer(self, open: ColLike, high: ColLike, low: ColLike,
                close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlhammer_feature import CDLHAMMERFeature
    return CDLHAMMERFeature(open, high, low, close)

  def cdlrisefall3methods(self, open: ColLike, high: ColLike, low: ColLike,
                          close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlrisefall3methods_feature import CDLRISEFALL3METHODSFeature
    return CDLRISEFALL3METHODSFeature(open, high, low, close)

  def cdlhangingman(self, open: ColLike, high: ColLike, low: ColLike,
                    close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlhangingman_feature import CDLHANGINGMANFeature
    return CDLHANGINGMANFeature(open, high, low, close)

  def cdl3whitesoldiers(self, open: ColLike, high: ColLike, low: ColLike,
                        close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdl3whitesoldiers_feature import CDL3WHITESOLDIERSFeature
    return CDL3WHITESOLDIERSFeature(open, high, low, close)

  def cdleveningdojistar(self, open: ColLike, high: ColLike, low: ColLike,
                         close: ColLike, penetration: float) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdleveningdojistar_feature import CDLEVENINGDOJISTARFeature
    return CDLEVENINGDOJISTARFeature(open, high, low, close, penetration)

  def cdltakuri(self, open: ColLike, high: ColLike, low: ColLike,
                close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdltakuri_feature import CDLTAKURIFeature
    return CDLTAKURIFeature(open, high, low, close)

  def cdlharamicross(self, open: ColLike, high: ColLike, low: ColLike,
                     close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlharamicross_feature import CDLHARAMICROSSFeature
    return CDLHARAMICROSSFeature(open, high, low, close)

  def cdl3inside(self, open: ColLike, high: ColLike, low: ColLike,
                 close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdl3inside_feature import CDL3INSIDEFeature
    return CDL3INSIDEFeature(open, high, low, close)

  def cdlupsidegap2crows(self, open: ColLike, high: ColLike, low: ColLike,
                         close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlupsidegap2crows_feature import CDLUPSIDEGAP2CROWSFeature
    return CDLUPSIDEGAP2CROWSFeature(open, high, low, close)

  def cdlconcealbabyswall(self, open: ColLike, high: ColLike, low: ColLike,
                          close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlconcealbabyswall_feature import CDLCONCEALBABYSWALLFeature
    return CDLCONCEALBABYSWALLFeature(open, high, low, close)

  def cdlmatchinglow(self, open: ColLike, high: ColLike, low: ColLike,
                     close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlmatchinglow_feature import CDLMATCHINGLOWFeature
    return CDLMATCHINGLOWFeature(open, high, low, close)

  def cdlclosingmarubozu(self, open: ColLike, high: ColLike, low: ColLike,
                         close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlclosingmarubozu_feature import CDLCLOSINGMARUBOZUFeature
    return CDLCLOSINGMARUBOZUFeature(open, high, low, close)

  def cdlkickingbylength(self, open: ColLike, high: ColLike, low: ColLike,
                         close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlkickingbylength_feature import CDLKICKINGBYLENGTHFeature
    return CDLKICKINGBYLENGTHFeature(open, high, low, close)

  def cdlmarubozu(self, open: ColLike, high: ColLike, low: ColLike,
                  close: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.quadri.talib.cdlmarubozu_feature import CDLMARUBOZUFeature
    return CDLMARUBOZUFeature(open, high, low, close)

  def sarext(self, high: ColLike, low: ColLike, startvalue: float,
             offsetonreverse: float, accelerationinitlong: float,
             accelerationlong: float, accelerationmaxlong: float,
             accelerationinitshort: float, accelerationshort: float,
             accelerationmaxshort: float) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.sarext_feature import SAREXTFeature
    return SAREXTFeature(high, low, startvalue, offsetonreverse,
                         accelerationinitlong, accelerationlong,
                         accelerationmaxlong, accelerationinitshort,
                         accelerationshort, accelerationmaxshort)

  def minus_dm(self, low: ColLike, high: ColLike,
               timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.minus_dm_feature import MINUS_DMFeature
    return MINUS_DMFeature(low, high, timeperiod)

  def beta(self, high: ColLike, low: ColLike, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.beta_feature import BETAFeature
    return BETAFeature(high, low, timeperiod)

  def correl(self, high: ColLike, low: ColLike,
             timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.correl_feature import CORRELFeature
    return CORRELFeature(high, low, timeperiod)

  def aroon_0(self, high: ColLike, low: ColLike,
              timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.aroon_feature import AROON_0Feature
    return AROON_0Feature(high, low, timeperiod)

  def aroon_aroonup(self, high: ColLike, low: ColLike,
                    timeperiod: int) -> "FeatureGen":
    return self.aroon_0(high, low, timeperiod)

  def aroon_1(self, high: ColLike, low: ColLike,
              timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.aroon_feature import AROON_1Feature
    return AROON_1Feature(high, low, timeperiod)

  def aroon_aroondown(self, high: ColLike, low: ColLike,
                      timeperiod: int) -> "FeatureGen":
    return self.aroon_1(high, low, timeperiod)

  def plus_dm(self,
              high: ColLike,
              low: ColLike,
              timeperiod: int = 14) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.plus_dm_feature import PLUS_DMFeature
    return PLUS_DMFeature(high, low, timeperiod)

  def midprice(self, high: ColLike, low: ColLike,
               timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.midprice_feature import MIDPRICEFeature
    return MIDPRICEFeature(high, low, timeperiod)

  def aroonosc(self, high: ColLike, low: ColLike,
               timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.aroonosc_feature import AROONOSCFeature
    return AROONOSCFeature(high, low, timeperiod)

  def sar(self, high: ColLike, low: ColLike, acceleration: float,
          maximum: float) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.sar_feature import SARFeature
    return SARFeature(high, low, acceleration, maximum)

  def obv(self, close: ColLike, volume: ColLike) -> "FeatureGen":
    from declafe.pl.feature_gen.binary.talib.obv_feature import OBVFeature
    return OBVFeature(close, volume)
