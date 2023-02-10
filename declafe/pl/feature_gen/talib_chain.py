from declafe.pl.feature_gen.feature_gen import FeatureGen


class TalibChain:

  def __init__(self, feature: FeatureGen):
    super().__init__()
    self.feature = feature

  def ppo(self, fastperiod: int, slowperiod: int, matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ppo_feature import PPOFeature
    return PPOFeature(self.feature, fastperiod, slowperiod, matype)

  def trima(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.trima_feature import TRIMAFeature
    return TRIMAFeature(self.feature, timeperiod)

  def tema(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.tema_feature import TEMAFeature
    return TEMAFeature(self.feature, timeperiod)

  def ht_phasor_0(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ht_phasor_feature import HT_PHASOR_0Feature
    return HT_PHASOR_0Feature(self.feature)

  def ht_phasor_1(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ht_phasor_feature import HT_PHASOR_1Feature
    return HT_PHASOR_1Feature(self.feature)

  def ht_sine_0(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ht_sine_feature import HT_SINE_0Feature
    return HT_SINE_0Feature(self.feature)

  def ht_sine_1(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ht_sine_feature import HT_SINE_1Feature
    return HT_SINE_1Feature(self.feature)

  def wma(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.wma_feature import WMAFeature
    return WMAFeature(self.feature, timeperiod)

  def macdext_0(self, fastperiod: int, fastmatype: int, slowperiod: int,
                slowmatype: int, signalperiod: int,
                signalmatype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.macdext_feature import MACDEXT_0Feature
    return MACDEXT_0Feature(self.feature, fastperiod, fastmatype, slowperiod,
                            slowmatype, signalperiod, signalmatype)

  def macdext_1(self, fastperiod: int, fastmatype: int, slowperiod: int,
                slowmatype: int, signalperiod: int,
                signalmatype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.macdext_feature import MACDEXT_1Feature
    return MACDEXT_1Feature(self.feature, fastperiod, fastmatype, slowperiod,
                            slowmatype, signalperiod, signalmatype)

  def macdext_2(self, fastperiod: int, fastmatype: int, slowperiod: int,
                slowmatype: int, signalperiod: int,
                signalmatype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.macdext_feature import MACDEXT_2Feature
    return MACDEXT_2Feature(self.feature, fastperiod, fastmatype, slowperiod,
                            slowmatype, signalperiod, signalmatype)

  def bbands_0(self, timeperiod: int, nbdevup: float, nbdevdn: float,
               matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.bbands_feature import BBANDS_0Feature
    return BBANDS_0Feature(self.feature, timeperiod, nbdevup, nbdevdn, matype)

  def bbands_1(self, timeperiod: int, nbdevup: float, nbdevdn: float,
               matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.bbands_feature import BBANDS_1Feature
    return BBANDS_1Feature(self.feature, timeperiod, nbdevup, nbdevdn, matype)

  def bbands_2(self, timeperiod: int, nbdevup: float, nbdevdn: float,
               matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.bbands_feature import BBANDS_2Feature
    return BBANDS_2Feature(self.feature, timeperiod, nbdevup, nbdevdn, matype)

  def rsi(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.rsi_feature import RSIFeature
    return RSIFeature(self.feature, timeperiod)

  def stddev(self, timeperiod: int, nbdev: float) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.stddev_feature import STDDEVFeature
    return STDDEVFeature(self.feature, timeperiod, nbdev)

  def trix(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.trix_feature import TRIXFeature
    return TRIXFeature(self.feature, timeperiod)

  def mama_0(self, fastlimit: float, slowlimit: float) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.mama_feature import MAMA_0Feature
    return MAMA_0Feature(self.feature, fastlimit, slowlimit)

  def mama_1(self, fastlimit: float, slowlimit: float) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.mama_feature import MAMA_1Feature
    return MAMA_1Feature(self.feature, fastlimit, slowlimit)

  def ema(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ema_feature import EMAFeature
    return EMAFeature(self.feature, timeperiod)

  def ht_trendmode(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ht_trendmode_feature import HT_TRENDMODEFeature
    return HT_TRENDMODEFeature(self.feature)

  def ht_dcphase(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ht_dcphase_feature import HT_DCPHASEFeature
    return HT_DCPHASEFeature(self.feature)

  def ma(self, timeperiod: int, matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ma_feature import MAFeature
    return MAFeature(self.feature, timeperiod, matype)

  def ht_dcperiod(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ht_dcperiod_feature import HT_DCPERIODFeature
    return HT_DCPERIODFeature(self.feature)

  def macd_0(self, fastperiod: int, slowperiod: int,
             signalperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.macd_feature import MACD_0Feature
    return MACD_0Feature(self.feature, fastperiod, slowperiod, signalperiod)

  def macd_1(self, fastperiod: int, slowperiod: int,
             signalperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.macd_feature import MACD_1Feature
    return MACD_1Feature(self.feature, fastperiod, slowperiod, signalperiod)

  def macd_2(self, fastperiod: int, slowperiod: int,
             signalperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.macd_feature import MACD_2Feature
    return MACD_2Feature(self.feature, fastperiod, slowperiod, signalperiod)

  def kama(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.kama_feature import KAMAFeature
    return KAMAFeature(self.feature, timeperiod)

  def cmo(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.cmo_feature import CMOFeature
    return CMOFeature(self.feature, timeperiod)

  def t3(self, timeperiod: int, vfactor: float) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.t3_feature import T3Feature
    return T3Feature(self.feature, timeperiod, vfactor)

  def macdfix_0(self, signalperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.macdfix_feature import MACDFIX_0Feature
    return MACDFIX_0Feature(self.feature, signalperiod)

  def macdfix_1(self, signalperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.macdfix_feature import MACDFIX_1Feature
    return MACDFIX_1Feature(self.feature, signalperiod)

  def macdfix_2(self, signalperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.macdfix_feature import MACDFIX_2Feature
    return MACDFIX_2Feature(self.feature, signalperiod)

  def apo(self, fastperiod: int, slowperiod: int, matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.apo_feature import APOFeature
    return APOFeature(self.feature, fastperiod, slowperiod, matype)

  def mom(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.mom_feature import MOMFeature
    return MOMFeature(self.feature, timeperiod)

  def midpoint(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.midpoint_feature import MIDPOINTFeature
    return MIDPOINTFeature(self.feature, timeperiod)

  def dema(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.dema_feature import DEMAFeature
    return DEMAFeature(self.feature, timeperiod)

  def stochrsi_0(self, timeperiod: int, fastk_period: int, fastd_period: int,
                 fastd_matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.stochrsi_feature import STOCHRSI_0Feature
    return STOCHRSI_0Feature(self.feature, timeperiod, fastk_period,
                             fastd_period, fastd_matype)

  def stochrsi_1(self, timeperiod: int, fastk_period: int, fastd_period: int,
                 fastd_matype: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.stochrsi_feature import STOCHRSI_1Feature
    return STOCHRSI_1Feature(self.feature, timeperiod, fastk_period,
                             fastd_period, fastd_matype)

  def ht_trendline(self) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.ht_trendline_feature import HT_TRENDLINEFeature
    return HT_TRENDLINEFeature(self.feature)

  def sma(self, timeperiod: int) -> "FeatureGen":
    from declafe.pl.feature_gen.unary.talib.sma_feature import SMAFeature
    return SMAFeature(self.feature, timeperiod)
