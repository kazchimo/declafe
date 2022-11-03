from abc import abstractmethod
from typing import Type, TYPE_CHECKING, Any, List, TypeVar, cast, Callable, Literal

import numpy as np
import pandas as pd

if TYPE_CHECKING:
  from ..feature_gen import FeatureGen
  from declafe.feature_gen.Features import Features
  from declafe.feature_gen.unary import UnaryFeature
  from .. import ColLike


class ChainMixin:

  def __init__(self):
    from declafe.feature_gen.Features import Features
    self.FS = Features

  @abstractmethod
  def _self(self) -> "FeatureGen":
    raise NotImplementedError

  def next(self, f: Type["UnaryFeature"], *args, **kwargs) -> "FeatureGen":
    from declafe.feature_gen.ComposedFeature import ComposedFeature
    from declafe.feature_gen.unary import IdFeature

    _self = self._self()
    if isinstance(_self, IdFeature):
      return f(column_name=_self.column_name, *args, **kwargs)
    else:
      return ComposedFeature(
          head=_self,
          nexts=[f(column_name=_self.feature_name, *args, **kwargs)])

  def of_cond(self, true_col: "ColLike", false_col: "ColLike"):
    from declafe.feature_gen.tri.CondFeature import CondFeature
    return CondFeature(self._self(), true_col, false_col)

  def then(self, func: Callable[[pd.Series], pd.Series],
           op_name: str) -> "FeatureGen":
    from declafe.feature_gen.unary.FromFuncFeature import FromFuncFeature
    return self.next(FromFuncFeature, func=func, op_name=op_name)

  def accumulate(self, ops_name: str, ops_func: Callable[[Any, Any],
                                                         Any]) -> "FeatureGen":
    from declafe.feature_gen.unary.AccumulateFeature import AccumulateFeature
    return self.next(AccumulateFeature, ops_name=ops_name, ops_func=ops_func)

  def exist_within(self, target_value: Any, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary.ExistWithinFeature import ExistWithinFeature
    return self.next(ExistWithinFeature,
                     target_value=target_value,
                     period=period)

  def consecutive_count_of(self, target_value: Any) -> "FeatureGen":
    from declafe.feature_gen.unary import ConsecutiveCountFeature
    return self.next(ConsecutiveCountFeature, target_value=target_value)

  def consecutive_up_count(self) -> "FeatureGen":
    return self.is_up().consecutive_count_of(True).as_name_of(
        f"consecutive_up_count_of_{self._self().feature_name}")

  def consecutive_down_count(self) -> "FeatureGen":
    return self.is_down().consecutive_count_of(True).as_name_of(
        f"consecutive_down_count_of_{self._self().feature_name}")

  def log(self) -> "FeatureGen":
    from declafe.feature_gen.unary import LogFeature
    return self.next(LogFeature)

  def abs(self) -> "FeatureGen":
    from declafe.feature_gen.unary.AbsFeature import AbsFeature
    return self.next(AbsFeature)

  def is_up(self, period: int = 1) -> "FeatureGen":
    return ((self._self() - self.lag(1)) > 0).as_name_of(f"is_up{period}")

  def is_down(self, period: int = 1) -> "FeatureGen":
    return ((self._self() - self.lag(1)) < 0).as_name_of(f"is_down{period}")

  def moving_averages(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_average(p) for p in periods])

  def moving_average(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import MovingAverage
    return self.next(MovingAverage, periods=period)

  def moving_sums(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_sum(p) for p in periods])

  def moving_sum(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import SumFeature
    return self.next(SumFeature, periods=period)

  def ema(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import EMAFeature
    return self.next(EMAFeature, periods=period)

  def emas(self, periods: List[int]) -> "Features":
    return self.FS([self.ema(period) for period in periods])

  def dema(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import DEMAFeature
    return self.next(DEMAFeature, periods=period)

  def demas(self, periods: List[int]) -> "Features":
    return self.FS([self.dema(period) for period in periods])

  def cmo(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.CMOFeature import CMOFeature
    return self.next(CMOFeature, periods=period)

  def cmos(self, periods: List[int]) -> "Features":
    return self.FS([self.cmo(period) for period in periods])

  def wma(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import WeightedMovingAverage
    return self.next(WeightedMovingAverage, periods=period)

  def wmas(self, periods: List[int]) -> "Features":
    return self.FS([self.wma(period) for period in periods])

  def kamas(self, periods: List[int]) -> "Features":
    return self.FS([self.kama(period) for period in periods])

  def kama(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import KAMAFeature
    return self.next(KAMAFeature, periods=period)

  def mama(self) -> "FeatureGen":
    from declafe.feature_gen.unary import MAMAFeature
    return self.next(MAMAFeature)

  def fama(self) -> "FeatureGen":
    from declafe.feature_gen.unary import FAMAFeature
    return self.next(FAMAFeature)

  def tema(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import TEMAFeature
    return self.next(TEMAFeature, period=period)

  def temas(self, periods: List[int]) -> "Features":
    return self.FS([self.tema(period) for period in periods])

  def trima(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import TRIMAFeature
    return self.next(TRIMAFeature, period=period)

  def trimas(self, periods: List[int]) -> "Features":
    return self.FS([self.trima(period) for period in periods])

  def t3(self, period) -> "FeatureGen":
    from declafe.feature_gen.unary import T3Feature
    return self.next(T3Feature, period=period)

  def t3s(self, periods: List[int]) -> "Features":
    return self.FS([self.t3(period) for period in periods])

  def apo(self, fastperiod: int, slowperiod: int) -> "FeatureGen":
    from declafe.feature_gen.unary import APOFeature
    return self.next(APOFeature, fastperiod=fastperiod, slowperiod=slowperiod)

  def moving_midpoints(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_midpoint(p) for p in periods])

  def moving_midpoint(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import MidpointFeature
    return self.next(MidpointFeature, periods=period)

  def moving_stds(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_std(p) for p in periods])

  def moving_std(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import StddevFeature
    return self.next(StddevFeature, periods=period)

  def pct_changes(self, periods: List[int]) -> "Features":
    return self.FS([self.pct_change(p) for p in periods])

  def pct_change(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import PctChangeFeature
    return self.next(PctChangeFeature, periods=period)

  def lags(self, periods: List[int]) -> "Features":
    return self.FS([self.lag(p) for p in periods])

  def lag(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import LagFeature
    return self.next(LagFeature, periods=period)

  def moving_maxes(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_max(period) for period in periods])

  def moving_max(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import MaxFeature
    return self.next(MaxFeature, periods=period)

  def moving_mins(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_min(p) for p in periods])

  def moving_min(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary import MinFeature
    return self.next(MinFeature, periods=period)

  def min_comp(self, comp: float) -> "FeatureGen":
    from declafe.feature_gen.unary.MinCompFeature import MinCompFeature
    return self.next(MinCompFeature, comp=comp)

  def max_comp(self, comp: float) -> "FeatureGen":
    from declafe.feature_gen.unary.MaxCompFeature import MaxCompFeature
    return self.next(MaxCompFeature, comp=comp)

  def is_positive(self):
    from declafe.feature_gen.unary import IsPositiveFeature
    return self.next(IsPositiveFeature)

  def second(self) -> "FeatureGen":
    from declafe.feature_gen.unary.times.SecondFeature import SecondFeature
    return self.next(SecondFeature)

  def minute(self) -> "FeatureGen":
    from declafe.feature_gen.unary.times import MinuteFeature
    return self.next(MinuteFeature)

  def minute_n(self, n: int) -> "FeatureGen":
    return ((self.minute() % n) == 0)\
      .as_bool()\
      .as_name_of(f"minute_{n}_of_{self._self().feature_name}")

  def minute_ns(self, ns: List[int]) -> "Features":
    return self.FS([self.minute_n(n) for n in ns])

  def hour(self):
    from declafe.feature_gen.unary.times import HourFeature
    return self.next(HourFeature)

  def hour_n(self, n: int) -> "FeatureGen":
    return ((self.hour() % n) == 0)\
      .as_bool()\
      .as_name_of(f"hour_{n}_of_{self._self().feature_name}")

  def hour_ns(self, ns: List[int]) -> "Features":
    return self.FS([self.hour_n(n) for n in ns])

  def day_of_week(self) -> "FeatureGen":
    from declafe.feature_gen.unary.times import DayOfWeekFeature
    return self.next(DayOfWeekFeature)

  def week_of_year(self) -> "FeatureGen":
    from declafe.feature_gen.unary.times import WeekOfYearFeature
    return self.next(WeekOfYearFeature)

  def day_of_month(self) -> "FeatureGen":
    from declafe.feature_gen.unary.times import DayOfMonthFeature
    return self.next(DayOfMonthFeature)

  def month(self) -> "FeatureGen":
    from declafe.feature_gen.unary.times import MonthFeature
    return self.next(MonthFeature)

  def to_datetime(self, unit: Literal["D", "s", "ms", "us",
                                      "ns"]) -> "FeatureGen":
    from declafe.feature_gen.unary.times.ToDatetimeFeature import ToDatetimeFeature
    return self.next(ToDatetimeFeature, unit=unit)

  def flip_bool(self):
    from declafe.feature_gen.unary import FlipBoolFeature
    return self.next(FlipBoolFeature)

  def bbands_uppers(self, periods: List[int], nbdevup: float) -> "Features":
    return self.FS([self.bbands_upper(period, nbdevup) for period in periods])

  def bbands_upper(self, period: int, nbdevup: float) -> "FeatureGen":
    from declafe.feature_gen.unary import BBandsUpperFeature
    return self.next(BBandsUpperFeature, periods=period, nbdevup=nbdevup)

  def bbands_lowers(self, periods: List[int], nbdevdn: float) -> "Features":
    return self.FS([self.bbands_lower(period, nbdevdn) for period in periods])

  def bbands_lower(self, period: int, nbdevdn: float) -> "FeatureGen":
    from declafe.feature_gen.unary import BBandsLowerFeature
    return self.next(BBandsLowerFeature, periods=period, nbdevdn=nbdevdn)

  def macd(self, fastperiod: int, slowperiod: int,
           signalperiod: int) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.MACDFeature import MACDFeature
    return self.next(MACDFeature,
                     fastperiod=fastperiod,
                     slowperiod=slowperiod,
                     signalperiod=signalperiod)

  def macd_signal(self, fastperiod: int, slowperiod: int,
                  signalperiod: int) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.MACDFeature import MACDSignalFeature
    return self.next(MACDSignalFeature,
                     fastperiod=fastperiod,
                     slowperiod=slowperiod,
                     signalperiod=signalperiod)

  def macd_hist(self, fastperiod: int, slowperiod: int,
                signalperiod: int) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.MACDFeature import MACDHistFeature
    return self.next(MACDHistFeature,
                     fastperiod=fastperiod,
                     slowperiod=slowperiod,
                     signalperiod=signalperiod)

  def mom(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.MOMFeature import MOMFeature
    return self.next(MOMFeature, period=period)

  def moms(self, periods: List[int]) -> "Features":
    return self.FS([self.mom(period) for period in periods])

  def ppo(self, fast_period: int, slow_period: int) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.PPOFeature import PPOFeature
    return self.next(PPOFeature,
                     fast_period=fast_period,
                     slow_period=slow_period)

  def rsi(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.RSIFeature import RSIFeature
    return self.next(RSIFeature, period=period)

  def rsis(self, periods: List[int]) -> "Features":
    return self.FS([self.rsi(period) for period in periods])

  def stochrsi_fastk(self,
                     period: int,
                     fastk_period: int,
                     fastd_period: int,
                     fastd_matype: int = 0) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.STOCHRSI import STOCHRSIFastkFeature
    return self.next(STOCHRSIFastkFeature,
                     period=period,
                     fastk_period=fastk_period,
                     fastd_period=fastd_period,
                     fastd_matype=fastd_matype)

  def stochrsi_fastks(self,
                      periods: List[int],
                      fastk_period: int,
                      fastd_period: int,
                      fastd_matype: int = 0) -> "Features":
    return self.FS([
        self.stochrsi_fastk(period, fastk_period, fastd_period, fastd_matype)
        for period in periods
    ])

  def stochrsi_fastd(self,
                     period: int,
                     fastk_period: int,
                     fastd_period: int,
                     fastd_matype: int = 0) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.STOCHRSI import STOCHRSIFastdFeature
    return self.next(STOCHRSIFastdFeature,
                     period=period,
                     fastk_period=fastk_period,
                     fastd_period=fastd_period,
                     fastd_matype=fastd_matype)

  def stochrsi_fastds(self,
                      periods: List[int],
                      fastk_period: int,
                      fastd_period: int,
                      fastd_matype: int = 0) -> "Features":
    return self.FS([
        self.stochrsi_fastd(period, fastk_period, fastd_period, fastd_matype)
        for period in periods
    ])

  def trix(self, period: int) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.TrixFeature import TRIXFeature
    return self.next(TRIXFeature, period=period)

  def trixes(self, periods: List[int]) -> "Features":
    return self.FS([self.trix(period) for period in periods])

  def round_n(self, round_digit: int) -> "FeatureGen":
    from declafe.feature_gen.unary import RoundNFeature
    return self.next(RoundNFeature, round_digit=round_digit)

  T = TypeVar("T")

  def replace(self, target_value: T, to_value: T) -> "FeatureGen":
    from declafe.feature_gen.unary.ReplaceFeature import ReplaceFeature
    return self.next(ReplaceFeature,
                     target_value=target_value,
                     to_value=to_value)

  def replace_na(self, to_value: Any) -> "FeatureGen":
    return self.replace(np.nan, to_value)

  def max_with(self, col: "ColLike") -> "FeatureGen":
    from declafe.feature_gen.binary.MaxWith import MaxWithFeature
    return MaxWithFeature(cast("FeatureGen", self), col)

  def min_with(self, col: "ColLike") -> "FeatureGen":
    from declafe.feature_gen.binary.MinWith import MinWithFeature
    return MinWithFeature(cast("FeatureGen", self), col)

  def ht_dcperiod(self) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.HT_DCPERIODFeature import HT_DCPERIODFeature
    return self.next(HT_DCPERIODFeature)

  def ht_dcphase(self) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.HT_DCPHASEFeature import HT_DCPHASEFeature
    return self.next(HT_DCPHASEFeature)

  def ht_phasor_inphase(self) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.HT_PHASORFeature import HT_PHASORInphaseFeature
    return self.next(HT_PHASORInphaseFeature)

  def ht_phasor_quadrature(self) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.HT_PHASORFeature import HT_PHASORQuadratureFeature
    return self.next(HT_PHASORQuadratureFeature)

  def ht_sine(self) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.HTSineFeature import HTSineFeature
    return self.next(HTSineFeature)

  def ht_leadsine(self) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.HTSineFeature import HTLeadsineFeature
    return self.next(HTLeadsineFeature)

  def ht_trendmode(self) -> "FeatureGen":
    from declafe.feature_gen.unary.talib.HTTrendmodeFeature import HTTrendModeFeature
    return self.next(HTTrendModeFeature)

  def __invert__(self) -> "FeatureGen":
    from declafe.feature_gen.unary.NotFeature import NotFeature
    return self.next(NotFeature)
