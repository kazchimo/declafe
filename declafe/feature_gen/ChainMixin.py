from typing import Type, TYPE_CHECKING, Any, List

if TYPE_CHECKING:
  from declafe import UnaryColumnFeature, FeatureGen, Features


class ChainMixin:

  def __init__(self):
    from declafe import Features
    self.FS = Features

  def next(
      self: "FeatureGen", f: Type["UnaryColumnFeature"], *args,
      **kwargs) -> "FeatureGen":
    from declafe.ComposedFeature import ComposedFeature
    from declafe.unary import IdFeature

    if isinstance(self, IdFeature):
      return f(column_name=self.column_name, *args, **kwargs)
    else:
      return ComposedFeature(
          head=self, nexts=[f(column_name=self.feature_name, *args, **kwargs)])

  def consecutive_count_of(self, target_value: Any) -> "FeatureGen":
    from declafe.unary import ConsecutiveCountFeature
    return self.next(ConsecutiveCountFeature, target_value=target_value)

  def consecutive_up_count(self: "FeatureGen") -> "FeatureGen":
    return self.is_up().consecutive_count_of(True).as_name_of(
        f"consecutive_up_count_of_{self.feature_name}")

  def consecutive_down_count(self: "FeatureGen") -> "FeatureGen":
    return self.is_down().consecutive_count_of(True).as_name_of(
        f"consecutive_down_count_of_{self.feature_name}")

  def log(self) -> "FeatureGen":
    from declafe.unary import LogFeature
    return self.next(LogFeature)

  def is_up(self, period: int = 1) -> "FeatureGen":
    return (self.pct_change(period) > 0).as_name_of(f"is_up{period}")

  def is_down(self, period: int = 1) -> "FeatureGen":
    return (self.pct_change(period) < 0).as_name_of(f"is_down{period}")

  def moving_averages(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_average(p) for p in periods])

  def moving_average(self, period: int) -> "FeatureGen":
    from declafe.unary import MovingAverage
    return self.next(MovingAverage, periods=period)

  def moving_sums(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_sum(p) for p in periods])

  def moving_sum(self, period: int) -> "FeatureGen":
    from declafe.unary import SumFeature
    return self.next(SumFeature, periods=period)

  def ema(self, period: int) -> "FeatureGen":
    from declafe.unary import EMAFeature
    return self.next(EMAFeature, periods=period)

  def emas(self, periods: List[int]) -> "Features":
    return self.FS([self.ema(period) for period in periods])

  def wma(self, period: int) -> "FeatureGen":
    from declafe.unary import WeightedMovingAverage
    return self.next(WeightedMovingAverage, periods=period)

  def wmas(self, periods: List[int]) -> "Features":
    return self.FS([self.wma(period) for period in periods])

  def kamas(self, periods: List[int]) -> "Features":
    return self.FS([self.kama(period) for period in periods])

  def kama(self, period: int) -> "FeatureGen":
    from declafe.unary import KAMAFeature
    return self.next(KAMAFeature, periods=period)

  def mama(self) -> "FeatureGen":
    from declafe.unary import MAMAFeature
    return self.next(MAMAFeature)

  def fama(self) -> "FeatureGen":
    from declafe.unary import FAMAFeature
    return self.next(FAMAFeature)

  def tema(self, period: int) -> "FeatureGen":
    from declafe.unary import TEMAFeature
    return self.next(TEMAFeature, period=period)

  def temas(self, periods: List[int]) -> "Features":
    return self.FS([self.tema(period) for period in periods])

  def trima(self, period: int) -> "FeatureGen":
    from declafe.unary import TRIMAFeature
    return self.next(TRIMAFeature, period=period)

  def trimas(self, periods: List[int]) -> "Features":
    return self.FS([self.trima(period) for period in periods])

  def t3(self, period) -> "FeatureGen":
    from declafe.unary import T3Feature
    return self.next(T3Feature, period=period)

  def t3s(self, periods: List[int]) -> "Features":
    return self.FS([self.t3(period) for period in periods])

  def apo(self) -> "FeatureGen":
    from declafe.unary import APOFeature
    return self.next(APOFeature)

  def moving_midpoints(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_midpoint(p) for p in periods])

  def moving_midpoint(self, period: int) -> "FeatureGen":
    from declafe.unary import MidpointFeature
    return self.next(MidpointFeature, periods=period)

  def moving_stds(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_std(p) for p in periods])

  def moving_std(self, period: int) -> "FeatureGen":
    from declafe.unary import StddevFeature
    return self.next(StddevFeature, periods=period)

  def pct_changes(self, periods: List[int]) -> "Features":
    return self.FS([self.pct_change(p) for p in periods])

  def pct_change(self, period: int) -> "FeatureGen":
    from declafe.unary import PctChangeFeature
    return self.next(PctChangeFeature, periods=period)

  def lags(self, periods: List[int]) -> "Features":
    return self.FS([self.lag(p) for p in periods])

  def lag(self, period: int) -> "FeatureGen":
    from declafe.unary import LagFeature
    return self.next(LagFeature, periods=period)

  def moving_maxes(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_max(period) for period in periods])

  def moving_max(self, period: int) -> "FeatureGen":
    from declafe.unary import MaxFeature
    return self.next(MaxFeature, periods=period)

  def moving_mins(self, periods: List[int]) -> "Features":
    return self.FS([self.moving_min(p) for p in periods])

  def moving_min(self, period: int) -> "FeatureGen":
    from declafe.unary import MinFeature
    return self.next(MinFeature, periods=period)

  def is_positive(self):
    from declafe.unary import IsPositiveFeature
    return self.next(IsPositiveFeature)

  def minute(self):
    from declafe.unary.times import MinuteFeature
    return self.next(MinuteFeature)

  def hour(self):
    from declafe.unary.times import HourFeature
    return self.next(HourFeature)

  def flip_bool(self):
    from declafe.unary import FlipBoolFeature
    return self.next(FlipBoolFeature)

  def bbands_uppers(self, periods: List[int]) -> "Features":
    return self.FS([self.bbands_upper(period) for period in periods])

  def bbands_upper(self, period: int) -> "FeatureGen":
    from declafe.unary import BBandsUpperFeature
    return self.next(BBandsUpperFeature, periods=period)

  def bbands_lowers(self, periods: List[int]) -> "Features":
    return self.FS([self.bbands_lower(period) for period in periods])

  def bbands_lower(self, period: int) -> "FeatureGen":
    from declafe.unary import BBandsLowerFeature
    return self.next(BBandsLowerFeature, periods=period)
