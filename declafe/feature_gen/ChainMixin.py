from abc import abstractmethod
from typing import TYPE_CHECKING, Any, List

if TYPE_CHECKING:
  from ..feature_gen import FeatureGen
  from ..Features import Features
  from ..unary import UnaryColumnFeature


class ChainMixin:

  def __init__(self):
    from ..Features import Features
    self.FS = Features

  @abstractmethod
  def _self(self) -> "FeatureGen":
    raise NotImplementedError

  def next(self, f: "UnaryColumnFeature") -> "FeatureGen":
    from ..ComposedFeature import ComposedFeature
    from ..unary import IdFeature

    _self = self._self()
    if isinstance(_self, IdFeature):
      return f
    else:
      return ComposedFeature(head=_self, nexts=[f])

  def consecutive_count_of(self, target_value: Any) -> "FeatureGen":
    from ..unary import ConsecutiveCountFeature
    return self.next(
        ConsecutiveCountFeature(target_value=target_value,
                                column_name=self._self().feature_name))

  def consecutive_up_count(self) -> "FeatureGen":
    return self.is_up().consecutive_count_of(True).as_name_of(
        f"consecutive_up_count_of_{self._self().feature_name}")

  def consecutive_down_count(self) -> "FeatureGen":
    return self.is_down().consecutive_count_of(True).as_name_of(
        f"consecutive_down_count_of_{self._self().feature_name}")

  def log(self) -> "FeatureGen":
    from ..unary import LogFeature
    return self.next(LogFeature(column_name=self._self().feature_name))

  def is_up(self, period: int = 1) -> "FeatureGen":
    return (self.pct_change(period) > 0).as_name_of(f"is_up{period}")

  def is_down(self, period: int = 1) -> "FeatureGen":
    return (self.pct_change(period) < 0).as_name_of(f"is_down{period}")

  def moving_averages(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_average(p) for p in periods])

  def moving_average(self, period: int) -> "FeatureGen":
    from ..unary import MovingAverage
    return self.next(
        MovingAverage(periods=period, column_name=self._self().feature_name))

  def moving_sums(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_sum(p) for p in periods])

  def moving_sum(self, period: int) -> "FeatureGen":
    from ..unary import SumFeature
    return self.next(
        SumFeature(periods=period, column_name=self._self().feature_name))

  def ema(self, period: int) -> "FeatureGen":
    from ..unary import EMAFeature
    return self.next(
        EMAFeature(periods=period, column_name=self._self().feature_name))

  def emas(self, periods: List[int]) -> "Features":
    return self.FS([self.ema(period) for period in periods])

  def wma(self, period: int) -> "FeatureGen":
    from ..unary import WeightedMovingAverage
    return self.next(
        WeightedMovingAverage(periods=period,
                              column_name=self._self().feature_name))

  def wmas(self, periods: List[int]) -> "Features":
    return self.FS([self.wma(period) for period in periods])

  def kamas(self, periods: List[int]) -> "Features":
    return self.FS([self.kama(period) for period in periods])

  def kama(self, period: int) -> "FeatureGen":
    from ..unary import KAMAFeature
    return self.next(
        KAMAFeature(periods=period, column_name=self._self().feature_name))

  def mama(self) -> "FeatureGen":
    from ..unary import MAMAFeature
    return self.next(MAMAFeature(column_name=self._self().feature_name))

  def fama(self) -> "FeatureGen":
    from ..unary import FAMAFeature
    return self.next(FAMAFeature(column_name=self._self().feature_name))

  def tema(self, period: int) -> "FeatureGen":
    from ..unary import TEMAFeature
    return self.next(
        TEMAFeature(period=period, column_name=self._self().feature_name))

  def temas(self, periods: List[int]) -> "Features":
    return self.FS([self.tema(period) for period in periods])

  def trima(self, period: int) -> "FeatureGen":
    from ..unary import TRIMAFeature
    return self.next(
        TRIMAFeature(period=period, column_name=self._self().feature_name))

  def trimas(self, periods: List[int]) -> "Features":
    return self.FS([self.trima(period) for period in periods])

  def t3(self, period) -> "FeatureGen":
    from ..unary import T3Feature
    return self.next(
        T3Feature(period=period, column_name=self._self().feature_name))

  def t3s(self, periods: List[int]) -> "Features":
    return self.FS([self.t3(period) for period in periods])

  def apo(self) -> "FeatureGen":
    from ..unary import APOFeature
    return self.next(APOFeature(column_name=self._self().feature_name))

  def moving_midpoints(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_midpoint(p) for p in periods])

  def moving_midpoint(self, period: int) -> "FeatureGen":
    from ..unary import MidpointFeature
    return self.next(
        MidpointFeature(periods=period, column_name=self._self().feature_name))

  def moving_stds(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_std(p) for p in periods])

  def moving_std(self, period: int) -> "FeatureGen":
    from ..unary import StddevFeature
    return self.next(
        StddevFeature(periods=period, column_name=self._self().feature_name))

  def pct_changes(self, periods: List[int]) -> "Features":
    return self.FS([self.pct_change(p) for p in periods])

  def pct_change(self, period: int) -> "FeatureGen":
    from ..unary import PctChangeFeature
    return self.next(
        PctChangeFeature(periods=period, column_name=self._self().feature_name))

  def lags(self, periods: List[int]) -> "Features":
    return self.FS([self.lag(p) for p in periods])

  def lag(self, period: int) -> "FeatureGen":
    from ..unary import LagFeature
    return self.next(
        LagFeature(periods=period, column_name=self._self().feature_name))

  def moving_maxes(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_max(period) for period in periods])

  def moving_max(self, period: int) -> "FeatureGen":
    from ..unary import MaxFeature
    return self.next(
        MaxFeature(periods=period, column_name=self._self().feature_name))

  def moving_mins(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_min(p) for p in periods])

  def moving_min(self, period: int) -> "FeatureGen":
    from ..unary import MinFeature
    return self.next(
        MinFeature(periods=period, column_name=self._self().feature_name))

  def is_positive(self):
    from ..unary import IsPositiveFeature
    return self.next(IsPositiveFeature(column_name=self._self().feature_name))

  def minute(self):
    from ..unary.times import MinuteFeature
    return self.next(MinuteFeature(column_name=self._self().feature_name))

  def hour(self):
    from ..unary.times import HourFeature
    return self.next(HourFeature(column_name=self._self().feature_name))

  def flip_bool(self):
    from ..unary import FlipBoolFeature
    return self.next(FlipBoolFeature(column_name=self._self().feature_name))

  def bbands_uppers(self, periods: List[int]) -> "Features":
    return self.FS([self.bbands_upper(period) for period in periods])

  def bbands_upper(self, period: int) -> "FeatureGen":
    from ..unary import BBandsUpperFeature
    return self.next(
        BBandsUpperFeature(periods=period,
                           column_name=self._self().feature_name))

  def bbands_lowers(self, periods: List[int]) -> "Features":
    return self.FS([self.bbands_lower(period) for period in periods])

  def bbands_lower(self, period: int) -> "FeatureGen":
    from ..unary import BBandsLowerFeature
    return self.next(
        BBandsLowerFeature(periods=period,
                           column_name=self._self().feature_name))

  def round_n(self, round_digit: int) -> "FeatureGen":
    from ..unary import RoundNFeature
    return self.next(
        RoundNFeature(round_digit=round_digit,
                      column_name=self._self().feature_name))
