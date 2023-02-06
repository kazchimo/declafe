from pl.feature_gen.types import ColLike
from pl.feature_gen.feature_gen import FeatureGen


# noinspection PyMethodMayBeStatic,SpellCheckingInspection
class TalibConstructor:

  def __init__(self):
    super().__init__()

  def dx(self, col1: ColLike, col2: ColLike, col3: ColLike,
         timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.tri.talib.dx_feature import DXFeature
    return DXFeature(col1, col2, col3, timeperiod)

  def trange(self, col1: ColLike, col2: ColLike, col3: ColLike) -> "FeatureGen":
    from pl.feature_gen.tri.talib.trange_feature import TRANGEFeature
    return TRANGEFeature(col1, col2, col3)

  def natr(self,
           col1: ColLike,
           col2: ColLike,
           col3: ColLike,
           timeperiod: int = 14) -> "FeatureGen":
    from pl.feature_gen.tri.talib.natr_feature import NATRFeature
    return NATRFeature(col1, col2, col3, timeperiod)

  def willr(self,
            col1: ColLike,
            col2: ColLike,
            col3: ColLike,
            timeperiod: int = 14) -> "FeatureGen":
    from pl.feature_gen.tri.talib.willr_feature import WILLRFeature
    return WILLRFeature(col1, col2, col3, timeperiod)

  def adxr(self, col1: ColLike, col2: ColLike, col3: ColLike,
           timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.tri.talib.adxr_feature import ADXRFeature
    return ADXRFeature(col1, col2, col3, timeperiod)

  def stoch_0(self, col1: ColLike, col2: ColLike, col3: ColLike,
              fastk_period: int, slowk_period: int, slowk_matype: int,
              slowd_period: int, slowd_matype: int) -> "FeatureGen":
    from pl.feature_gen.tri.talib.stoch_feature import STOCH_0Feature
    return STOCH_0Feature(col1, col2, col3, fastk_period, slowk_period,
                          slowk_matype, slowd_period, slowd_matype)

  def stoch_1(self, col1: ColLike, col2: ColLike, col3: ColLike,
              fastk_period: int, slowk_period: int, slowk_matype: int,
              slowd_period: int, slowd_matype: int) -> "FeatureGen":
    from pl.feature_gen.tri.talib.stoch_feature import STOCH_1Feature
    return STOCH_1Feature(col1, col2, col3, fastk_period, slowk_period,
                          slowk_matype, slowd_period, slowd_matype)

  def minus_di(self, col1: ColLike, col2: ColLike, col3: ColLike,
               timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.tri.talib.minus_di_feature import MINUS_DIFeature
    return MINUS_DIFeature(col1, col2, col3, timeperiod)

  def stochf_0(self, col1: ColLike, col2: ColLike, col3: ColLike,
               fastk_period: int, fastd_period: int,
               fastd_matype: int) -> "FeatureGen":
    from pl.feature_gen.tri.talib.stochf_feature import STOCHF_0Feature
    return STOCHF_0Feature(col1, col2, col3, fastk_period, fastd_period,
                           fastd_matype)

  def stochf_1(self, col1: ColLike, col2: ColLike, col3: ColLike,
               fastk_period: int, fastd_period: int,
               fastd_matype: int) -> "FeatureGen":
    from pl.feature_gen.tri.talib.stochf_feature import STOCHF_1Feature
    return STOCHF_1Feature(col1, col2, col3, fastk_period, fastd_period,
                           fastd_matype)

  def cci(self, col1: ColLike, col2: ColLike, col3: ColLike,
          timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.tri.talib.cci_feature import CCIFeature
    return CCIFeature(col1, col2, col3, timeperiod)

  def ultosc(self,
             col1: ColLike,
             col2: ColLike,
             col3: ColLike,
             timeperiod1: int = 7,
             timeperiod2: int = 14,
             timeperiod3: int = 28) -> "FeatureGen":
    from pl.feature_gen.tri.talib.ultosc_feature import ULTOSCFeature
    return ULTOSCFeature(col1, col2, col3, timeperiod1, timeperiod2,
                         timeperiod3)

  def atr(self,
          col1: ColLike,
          col2: ColLike,
          col3: ColLike,
          timeperiod: int = 14) -> "FeatureGen":
    from pl.feature_gen.tri.talib.atr_feature import ATRFeature
    return ATRFeature(col1, col2, col3, timeperiod)

  def plus_di(self,
              col1: ColLike,
              col2: ColLike,
              col3: ColLike,
              timeperiod: int = 14) -> "FeatureGen":
    from pl.feature_gen.tri.talib.plus_di_feature import PLUS_DIFeature
    return PLUS_DIFeature(col1, col2, col3, timeperiod)

  def adx(self, col1: ColLike, col2: ColLike, col3: ColLike,
          timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.tri.talib.adx_feature import ADXFeature
    return ADXFeature(col1, col2, col3, timeperiod)

  def cdlbreakaway(self, col1: ColLike, col2: ColLike, col3: ColLike,
                   col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlbreakaway_feature import CDLBREAKAWAYFeature
    return CDLBREAKAWAYFeature(col1, col2, col3, col4)

  def cdlrickshawman(self, col1: ColLike, col2: ColLike, col3: ColLike,
                     col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlrickshawman_feature import CDLRICKSHAWMANFeature
    return CDLRICKSHAWMANFeature(col1, col2, col3, col4)

  def cdlmorningdojistar(self,
                         col1: ColLike,
                         col2: ColLike,
                         col3: ColLike,
                         col4: ColLike,
                         penetration: float = 0) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlmorningdojistar_feature import CDLMORNINGDOJISTARFeature
    return CDLMORNINGDOJISTARFeature(col1, col2, col3, col4, penetration)

  def cdl3starsinsouth(self, col1: ColLike, col2: ColLike, col3: ColLike,
                       col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdl3starsinsouth_feature import CDL3STARSINSOUTHFeature
    return CDL3STARSINSOUTHFeature(col1, col2, col3, col4)

  def cdlladderbottom(self, col1: ColLike, col2: ColLike, col3: ColLike,
                      col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlladderbottom_feature import CDLLADDERBOTTOMFeature
    return CDLLADDERBOTTOMFeature(col1, col2, col3, col4)

  def cdldarkcloudcover(self, col1: ColLike, col2: ColLike, col3: ColLike,
                        col4: ColLike, penetration: float) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdldarkcloudcover_feature import CDLDARKCLOUDCOVERFeature
    return CDLDARKCLOUDCOVERFeature(col1, col2, col3, col4, penetration)

  def cdlpiercing(self, col1: ColLike, col2: ColLike, col3: ColLike,
                  col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlpiercing_feature import CDLPIERCINGFeature
    return CDLPIERCINGFeature(col1, col2, col3, col4)

  def cdlstalledpattern(self, col1: ColLike, col2: ColLike, col3: ColLike,
                        col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlstalledpattern_feature import CDLSTALLEDPATTERNFeature
    return CDLSTALLEDPATTERNFeature(col1, col2, col3, col4)

  def cdlinneck(self, col1: ColLike, col2: ColLike, col3: ColLike,
                col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlinneck_feature import CDLINNECKFeature
    return CDLINNECKFeature(col1, col2, col3, col4)

  def cdlgravestonedoji(self, col1: ColLike, col2: ColLike, col3: ColLike,
                        col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlgravestonedoji_feature import CDLGRAVESTONEDOJIFeature
    return CDLGRAVESTONEDOJIFeature(col1, col2, col3, col4)

  def cdl3linestrike(self, col1: ColLike, col2: ColLike, col3: ColLike,
                     col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdl3linestrike_feature import CDL3LINESTRIKEFeature
    return CDL3LINESTRIKEFeature(col1, col2, col3, col4)

  def cdlabandonedbaby(self, col1: ColLike, col2: ColLike, col3: ColLike,
                       col4: ColLike, penetration: float) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlabandonedbaby_feature import CDLABANDONEDBABYFeature
    return CDLABANDONEDBABYFeature(col1, col2, col3, col4, penetration)

  def cdl2crows(self, col1: ColLike, col2: ColLike, col3: ColLike,
                col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdl2crows_feature import CDL2CROWSFeature
    return CDL2CROWSFeature(col1, col2, col3, col4)

  def cdlunique3river(self, col1: ColLike, col2: ColLike, col3: ColLike,
                      col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlunique3river_feature import CDLUNIQUE3RIVERFeature
    return CDLUNIQUE3RIVERFeature(col1, col2, col3, col4)

  def cdl3blackcrows(self, col1: ColLike, col2: ColLike, col3: ColLike,
                     col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdl3blackcrows_feature import CDL3BLACKCROWSFeature
    return CDL3BLACKCROWSFeature(col1, col2, col3, col4)

  def mfi(self, col1: ColLike, col2: ColLike, col3: ColLike, col4: ColLike,
          timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.mfi_feature import MFIFeature
    return MFIFeature(col1, col2, col3, col4, timeperiod)

  def cdlhomingpigeon(self, col1: ColLike, col2: ColLike, col3: ColLike,
                      col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlhomingpigeon_feature import CDLHOMINGPIGEONFeature
    return CDLHOMINGPIGEONFeature(col1, col2, col3, col4)

  def adosc(self,
            col1: ColLike,
            col2: ColLike,
            col3: ColLike,
            col4: ColLike,
            fastperiod: int = 3,
            slowperiod: int = 10) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.adosc_feature import ADOSCFeature
    return ADOSCFeature(col1, col2, col3, col4, fastperiod, slowperiod)

  def cdlcounterattack(self, col1: ColLike, col2: ColLike, col3: ColLike,
                       col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlcounterattack_feature import CDLCOUNTERATTACKFeature
    return CDLCOUNTERATTACKFeature(col1, col2, col3, col4)

  def cdlidentical3crows(self, col1: ColLike, col2: ColLike, col3: ColLike,
                         col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlidentical3crows_feature import CDLIDENTICAL3CROWSFeature
    return CDLIDENTICAL3CROWSFeature(col1, col2, col3, col4)

  def cdlmorningstar(self,
                     col1: ColLike,
                     col2: ColLike,
                     col3: ColLike,
                     col4: ColLike,
                     penetration: float = 0) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlmorningstar_feature import CDLMORNINGSTARFeature
    return CDLMORNINGSTARFeature(col1, col2, col3, col4, penetration)

  def cdllongleggeddoji(self, col1: ColLike, col2: ColLike, col3: ColLike,
                        col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdllongleggeddoji_feature import CDLLONGLEGGEDDOJIFeature
    return CDLLONGLEGGEDDOJIFeature(col1, col2, col3, col4)

  def cdlseparatinglines(self, col1: ColLike, col2: ColLike, col3: ColLike,
                         col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlseparatinglines_feature import CDLSEPARATINGLINESFeature
    return CDLSEPARATINGLINESFeature(col1, col2, col3, col4)

  def cdlspinningtop(self, col1: ColLike, col2: ColLike, col3: ColLike,
                     col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlspinningtop_feature import CDLSPINNINGTOPFeature
    return CDLSPINNINGTOPFeature(col1, col2, col3, col4)

  def cdllongline(self, col1: ColLike, col2: ColLike, col3: ColLike,
                  col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdllongline_feature import CDLLONGLINEFeature
    return CDLLONGLINEFeature(col1, col2, col3, col4)

  def cdlinvertedhammer(self, col1: ColLike, col2: ColLike, col3: ColLike,
                        col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlinvertedhammer_feature import CDLINVERTEDHAMMERFeature
    return CDLINVERTEDHAMMERFeature(col1, col2, col3, col4)

  def cdlxsidegap3methods(self, col1: ColLike, col2: ColLike, col3: ColLike,
                          col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlxsidegap3methods_feature import CDLXSIDEGAP3METHODSFeature
    return CDLXSIDEGAP3METHODSFeature(col1, col2, col3, col4)

  def cdlengulfing(self, col1: ColLike, col2: ColLike, col3: ColLike,
                   col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlengulfing_feature import CDLENGULFINGFeature
    return CDLENGULFINGFeature(col1, col2, col3, col4)

  def cdlhikkakemod(self, col1: ColLike, col2: ColLike, col3: ColLike,
                    col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlhikkakemod_feature import CDLHIKKAKEMODFeature
    return CDLHIKKAKEMODFeature(col1, col2, col3, col4)

  def cdlharami(self, col1: ColLike, col2: ColLike, col3: ColLike,
                col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlharami_feature import CDLHARAMIFeature
    return CDLHARAMIFeature(col1, col2, col3, col4)

  def cdladvanceblock(self, col1: ColLike, col2: ColLike, col3: ColLike,
                      col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdladvanceblock_feature import CDLADVANCEBLOCKFeature
    return CDLADVANCEBLOCKFeature(col1, col2, col3, col4)

  def cdltasukigap(self, col1: ColLike, col2: ColLike, col3: ColLike,
                   col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdltasukigap_feature import CDLTASUKIGAPFeature
    return CDLTASUKIGAPFeature(col1, col2, col3, col4)

  def cdlonneck(self, col1: ColLike, col2: ColLike, col3: ColLike,
                col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlonneck_feature import CDLONNECKFeature
    return CDLONNECKFeature(col1, col2, col3, col4)

  def cdldojistar(self, col1: ColLike, col2: ColLike, col3: ColLike,
                  col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdldojistar_feature import CDLDOJISTARFeature
    return CDLDOJISTARFeature(col1, col2, col3, col4)

  def ad(self, col1: ColLike, col2: ColLike, col3: ColLike,
         col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.ad_feature import ADFeature
    return ADFeature(col1, col2, col3, col4)

  def cdlsticksandwich(self, col1: ColLike, col2: ColLike, col3: ColLike,
                       col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlsticksandwich_feature import CDLSTICKSANDWICHFeature
    return CDLSTICKSANDWICHFeature(col1, col2, col3, col4)

  def cdlshortline(self, col1: ColLike, col2: ColLike, col3: ColLike,
                   col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlshortline_feature import CDLSHORTLINEFeature
    return CDLSHORTLINEFeature(col1, col2, col3, col4)

  def cdl3outside(self, col1: ColLike, col2: ColLike, col3: ColLike,
                  col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdl3outside_feature import CDL3OUTSIDEFeature
    return CDL3OUTSIDEFeature(col1, col2, col3, col4)

  def cdlkicking(self, col1: ColLike, col2: ColLike, col3: ColLike,
                 col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlkicking_feature import CDLKICKINGFeature
    return CDLKICKINGFeature(col1, col2, col3, col4)

  def cdldragonflydoji(self, col1: ColLike, col2: ColLike, col3: ColLike,
                       col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdldragonflydoji_feature import CDLDRAGONFLYDOJIFeature
    return CDLDRAGONFLYDOJIFeature(col1, col2, col3, col4)

  def cdlhighwave(self, col1: ColLike, col2: ColLike, col3: ColLike,
                  col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlhighwave_feature import CDLHIGHWAVEFeature
    return CDLHIGHWAVEFeature(col1, col2, col3, col4)

  def cdlmathold(self,
                 col1: ColLike,
                 col2: ColLike,
                 col3: ColLike,
                 col4: ColLike,
                 penetration: float = 0) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlmathold_feature import CDLMATHOLDFeature
    return CDLMATHOLDFeature(col1, col2, col3, col4, penetration)

  def cdlhikkake(self, col1: ColLike, col2: ColLike, col3: ColLike,
                 col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlhikkake_feature import CDLHIKKAKEFeature
    return CDLHIKKAKEFeature(col1, col2, col3, col4)

  def cdldoji(self, col1: ColLike, col2: ColLike, col3: ColLike,
              col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdldoji_feature import CDLDOJIFeature
    return CDLDOJIFeature(col1, col2, col3, col4)

  def cdleveningstar(self, col1: ColLike, col2: ColLike, col3: ColLike,
                     col4: ColLike, penetration: float) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdleveningstar_feature import CDLEVENINGSTARFeature
    return CDLEVENINGSTARFeature(col1, col2, col3, col4, penetration)

  def cdlgapsidesidewhite(self, col1: ColLike, col2: ColLike, col3: ColLike,
                          col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlgapsidesidewhite_feature import CDLGAPSIDESIDEWHITEFeature
    return CDLGAPSIDESIDEWHITEFeature(col1, col2, col3, col4)

  def cdltristar(self, col1: ColLike, col2: ColLike, col3: ColLike,
                 col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdltristar_feature import CDLTRISTARFeature
    return CDLTRISTARFeature(col1, col2, col3, col4)

  def cdlthrusting(self, col1: ColLike, col2: ColLike, col3: ColLike,
                   col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlthrusting_feature import CDLTHRUSTINGFeature
    return CDLTHRUSTINGFeature(col1, col2, col3, col4)

  def cdlshootingstar(self, col1: ColLike, col2: ColLike, col3: ColLike,
                      col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlshootingstar_feature import CDLSHOOTINGSTARFeature
    return CDLSHOOTINGSTARFeature(col1, col2, col3, col4)

  def cdlbelthold(self, col1: ColLike, col2: ColLike, col3: ColLike,
                  col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlbelthold_feature import CDLBELTHOLDFeature
    return CDLBELTHOLDFeature(col1, col2, col3, col4)

  def bop(self, col1: ColLike, col2: ColLike, col3: ColLike,
          col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.bop_feature import BOPFeature
    return BOPFeature(col1, col2, col3, col4)

  def cdlhammer(self, col1: ColLike, col2: ColLike, col3: ColLike,
                col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlhammer_feature import CDLHAMMERFeature
    return CDLHAMMERFeature(col1, col2, col3, col4)

  def cdlrisefall3methods(self, col1: ColLike, col2: ColLike, col3: ColLike,
                          col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlrisefall3methods_feature import CDLRISEFALL3METHODSFeature
    return CDLRISEFALL3METHODSFeature(col1, col2, col3, col4)

  def cdlhangingman(self, col1: ColLike, col2: ColLike, col3: ColLike,
                    col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlhangingman_feature import CDLHANGINGMANFeature
    return CDLHANGINGMANFeature(col1, col2, col3, col4)

  def cdl3whitesoldiers(self, col1: ColLike, col2: ColLike, col3: ColLike,
                        col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdl3whitesoldiers_feature import CDL3WHITESOLDIERSFeature
    return CDL3WHITESOLDIERSFeature(col1, col2, col3, col4)

  def cdleveningdojistar(self, col1: ColLike, col2: ColLike, col3: ColLike,
                         col4: ColLike, penetration: float) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdleveningdojistar_feature import CDLEVENINGDOJISTARFeature
    return CDLEVENINGDOJISTARFeature(col1, col2, col3, col4, penetration)

  def cdltakuri(self, col1: ColLike, col2: ColLike, col3: ColLike,
                col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdltakuri_feature import CDLTAKURIFeature
    return CDLTAKURIFeature(col1, col2, col3, col4)

  def cdlharamicross(self, col1: ColLike, col2: ColLike, col3: ColLike,
                     col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlharamicross_feature import CDLHARAMICROSSFeature
    return CDLHARAMICROSSFeature(col1, col2, col3, col4)

  def cdl3inside(self, col1: ColLike, col2: ColLike, col3: ColLike,
                 col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdl3inside_feature import CDL3INSIDEFeature
    return CDL3INSIDEFeature(col1, col2, col3, col4)

  def cdlupsidegap2crows(self, col1: ColLike, col2: ColLike, col3: ColLike,
                         col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlupsidegap2crows_feature import CDLUPSIDEGAP2CROWSFeature
    return CDLUPSIDEGAP2CROWSFeature(col1, col2, col3, col4)

  def cdlconcealbabyswall(self, col1: ColLike, col2: ColLike, col3: ColLike,
                          col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlconcealbabyswall_feature import CDLCONCEALBABYSWALLFeature
    return CDLCONCEALBABYSWALLFeature(col1, col2, col3, col4)

  def cdlmatchinglow(self, col1: ColLike, col2: ColLike, col3: ColLike,
                     col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlmatchinglow_feature import CDLMATCHINGLOWFeature
    return CDLMATCHINGLOWFeature(col1, col2, col3, col4)

  def cdlclosingmarubozu(self, col1: ColLike, col2: ColLike, col3: ColLike,
                         col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlclosingmarubozu_feature import CDLCLOSINGMARUBOZUFeature
    return CDLCLOSINGMARUBOZUFeature(col1, col2, col3, col4)

  def cdlkickingbylength(self, col1: ColLike, col2: ColLike, col3: ColLike,
                         col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlkickingbylength_feature import CDLKICKINGBYLENGTHFeature
    return CDLKICKINGBYLENGTHFeature(col1, col2, col3, col4)

  def cdlmarubozu(self, col1: ColLike, col2: ColLike, col3: ColLike,
                  col4: ColLike) -> "FeatureGen":
    from pl.feature_gen.quadri.talib.cdlmarubozu_feature import CDLMARUBOZUFeature
    return CDLMARUBOZUFeature(col1, col2, col3, col4)

  def sarext(self, left: ColLike, right: ColLike, startvalue: float,
             offsetonreverse: float, accelerationinitlong: float,
             accelerationlong: float, accelerationmaxlong: float,
             accelerationinitshort: float, accelerationshort: float,
             accelerationmaxshort: float) -> "FeatureGen":
    from pl.feature_gen.binary.talib.sarext_feature import SAREXTFeature
    return SAREXTFeature(left, right, startvalue, offsetonreverse,
                         accelerationinitlong, accelerationlong,
                         accelerationmaxlong, accelerationinitshort,
                         accelerationshort, accelerationmaxshort)

  def minus_dm(self, left: ColLike, right: ColLike,
               timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.binary.talib.minus_dm_feature import MINUS_DMFeature
    return MINUS_DMFeature(left, right, timeperiod)

  def beta(self, left: ColLike, right: ColLike,
           timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.binary.talib.beta_feature import BETAFeature
    return BETAFeature(left, right, timeperiod)

  def correl(self, left: ColLike, right: ColLike,
             timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.binary.talib.correl_feature import CORRELFeature
    return CORRELFeature(left, right, timeperiod)

  def aroon_0(self, left: ColLike, right: ColLike,
              timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.binary.talib.aroon_feature import AROON_0Feature
    return AROON_0Feature(left, right, timeperiod)

  def aroon_1(self, left: ColLike, right: ColLike,
              timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.binary.talib.aroon_feature import AROON_1Feature
    return AROON_1Feature(left, right, timeperiod)

  def plus_dm(self,
              left: ColLike,
              right: ColLike,
              timeperiod: int = 14) -> "FeatureGen":
    from pl.feature_gen.binary.talib.plus_dm_feature import PLUS_DMFeature
    return PLUS_DMFeature(left, right, timeperiod)

  def midprice(self, left: ColLike, right: ColLike,
               timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.binary.talib.midprice_feature import MIDPRICEFeature
    return MIDPRICEFeature(left, right, timeperiod)

  def aroonosc(self, left: ColLike, right: ColLike,
               timeperiod: int) -> "FeatureGen":
    from pl.feature_gen.binary.talib.aroonosc_feature import AROONOSCFeature
    return AROONOSCFeature(left, right, timeperiod)

  def sar(self, left: ColLike, right: ColLike, acceleration: float,
          maximum: float) -> "FeatureGen":
    from pl.feature_gen.binary.talib.sar_feature import SARFeature
    return SARFeature(left, right, acceleration, maximum)

  def obv(self, left: ColLike, right: ColLike) -> "FeatureGen":
    from pl.feature_gen.binary.talib.obv_feature import OBVFeature
    return OBVFeature(left, right)
