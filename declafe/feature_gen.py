from abc import ABC, abstractmethod
from typing import Type, List, TYPE_CHECKING, Optional, Any

import pandas as pd

__all__ = ["FeatureGen", "FG"]

if TYPE_CHECKING:
  from declafe import ComposedFeature, BiComposeFeature, Features
  from declafe.unary import IdFeature
  from declafe.unary.UnaryColumnFeature import UnaryColumnFeature


class FeatureGen(ABC):
  def __init__(self):
    self.override_feature_name: Optional[str] = None

  @abstractmethod
  def gen(self, df: pd.DataFrame) -> pd.Series:
    raise NotImplementedError

  def generate(self, df: pd.DataFrame) -> pd.Series:
    """optimized gen"""
    if self.feature_name in df.columns:
      return df[self.feature_name]
    else:
      return self.gen(df)

  @abstractmethod
  def _feature_name(self) -> str:
    """
    各featureクラスをインスタンス化したときの名前
    e.g. PctChangeFeature(column_name="close", periods=5) => "pct_change_5_of_close"
    """
    raise NotImplementedError

  @property
  def feature_name(self) -> str:
    return self.override_feature_name or \
           (self._feature_name())

  def equals(self, other: "FeatureGen") -> bool:
    return self.feature_name == other.feature_name

  @property
  def to_features(self) -> "Features":
    from declafe import Features
    return Features.one(self)

  def to_features_with(self, other: "FeatureGen") -> "Features":
    return self.to_features.add_feature(other)

  def as_name_of(self, feature_name: str) -> "FeatureGen":
    self.override_feature_name = feature_name
    return self

  def set_feature(self, df: pd.DataFrame) -> None:
    df[self.feature_name] = self.generate(df)

  def next(self, f: Type["UnaryColumnFeature"], *args, **kwargs) -> "FeatureGen":
    from declafe.ComposedFeature import ComposedFeature
    from declafe.unary import IdFeature

    if isinstance(self, IdFeature):
      return f(column_name=self.column_name, *args, **kwargs)
    else:
      return ComposedFeature(head=self, nexts=[f(column_name=self.feature_name, *args, **kwargs)])

  def consecutive_count_of(self, target_value: Any) -> "FeatureGen":
    from declafe.unary import ConsecutiveCountFeature
    return self.next(ConsecutiveCountFeature, target_value=target_value)

  def consecutive_up_count(self) -> "FeatureGen":
    return self.is_up().consecutive_count_of(True).as_name_of(f"consecutive_up_count_of_{self.feature_name}")

  def consecutive_down_count(self) -> "FeatureGen":
    return self.is_down().consecutive_count_of(True).as_name_of(f"consecutive_down_count_of_{self.feature_name}")

  def log(self) -> "FeatureGen":
    from declafe.unary import LogFeature
    return self.next(LogFeature)

  def is_up(self, period: int = 1):
    return (self.pct_change(period) > 0).as_name_of(f"is_up{period}")

  def is_down(self, period: int = 1):
    return (self.pct_change(period) < 0).as_name_of(f"is_down{period}")

  def moving_averages(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.moving_average(p) for p in periods]

  def moving_average(self, period: int) -> "FeatureGen":
    from declafe.unary import MovingAverage
    return self.next(MovingAverage, periods=period)

  def moving_sums(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.moving_sum(p) for p in periods]

  def moving_sum(self, period: int) -> "FeatureGen":
    from declafe.unary import SumFeature
    return self.next(SumFeature, periods=period)

  def ema(self, period: int) -> "FeatureGen":
    from declafe.unary import EMAFeature
    return self.next(EMAFeature, periods=period)

  def emas(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.ema(period) for period in periods]

  def wma(self, period: int) -> "FeatureGen":
    from declafe.unary import WeightedMovingAverage
    return self.next(WeightedMovingAverage, periods=period)

  def wmas(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.wma(period) for period in periods]

  def kamas(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.kama(period) for period in periods]

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

  def temas(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.tema(period) for period in periods]

  def trima(self, period: int) -> "FeatureGen":
    from declafe.unary import TRIMAFeature
    return self.next(TRIMAFeature, period=period)

  def trimas(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.trima(period) for period in periods]

  def t3(self, period) -> "FeatureGen":
    from declafe.unary import T3Feature
    return self.next(T3Feature, period=period)

  def t3s(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.t3(period) for period in periods]

  def apo(self) -> "FeatureGen":
    from declafe.unary import APOFeature
    return self.next(APOFeature)

  def moving_midpoints(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.moving_midpoint(p) for p in periods]

  def moving_midpoint(self, period: int) -> "FeatureGen":
    from declafe.unary import MidpointFeature
    return self.next(MidpointFeature, periods=period)

  def moving_stds(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.moving_std(p) for p in periods]

  def moving_std(self, period: int) -> "FeatureGen":
    from declafe.unary import StddevFeature
    return self.next(StddevFeature, periods=period)

  def pct_changes(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.pct_change(p) for p in periods]

  def pct_change(self, period: int) -> "FeatureGen":
    from declafe.unary import PctChangeFeature
    return self.next(PctChangeFeature, periods=period)

  def lags(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.lag(p) for p in periods]

  def lag(self, period: int) -> "FeatureGen":
    from declafe.unary import LagFeature
    return self.next(LagFeature, periods=period)

  def moving_maxes(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.moving_max(period) for period in periods]

  def moving_max(self, period: int) -> "FeatureGen":
    from declafe.unary import MaxFeature
    return self.next(MaxFeature, periods=period)

  def moving_mins(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.moving_min(p) for p in periods]

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

  def bbands_uppers(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.bbands_upper(period) for period in periods]

  def bbands_upper(self, period: int) -> "FeatureGen":
    from declafe.unary import BBandsUpperFeature
    return self.next(BBandsUpperFeature, periods=period)

  def bbands_lowers(self, periods: List[int]) -> List["FeatureGen"]:
    return [self.bbands_lower(period) for period in periods]

  def bbands_lower(self, period: int) -> "FeatureGen":
    from declafe.unary import BBandsLowerFeature
    return self.next(BBandsLowerFeature, periods=period)

  def __eq__(self, other):
    from declafe.binary import EqualFeature, BiComposeFeature

    return BiComposeFeature.make(left=self, right=self.__conv_const(other), to=EqualFeature)

  def __ne__(self, other):
    return (self == other).flip_bool()

  def __add__(self, other):
    from declafe.binary import AddFeature
    from declafe import BiComposeFeature
    return BiComposeFeature.make(left=self, right=other, to=AddFeature)

  def __sub__(self, other):
    from declafe import BiComposeFeature
    from declafe.binary import SubFeature

    return BiComposeFeature.make(self, self.__conv_const(other), SubFeature)

  def __mul__(self, other):
    from declafe import BiComposeFeature
    from declafe.binary import ProductFeature

    return BiComposeFeature.make(self, self.__conv_const(other), ProductFeature)

  def __mod__(self, other):
    from declafe import BiComposeFeature
    from declafe.binary import ModFeature

    return BiComposeFeature.make(self, self.__conv_const(other), ModFeature)

  def __truediv__(self, other: "FeatureGen") -> "FeatureGen":
    from declafe import BiComposeFeature
    from declafe.binary import DivideFeature

    return BiComposeFeature.make(self, self.__conv_const(other), DivideFeature)

  def __gt__(self, other):
    from declafe import BiComposeFeature
    from declafe.binary import IsGreaterFeature

    return BiComposeFeature.make(self, self.__conv_const(other), IsGreaterFeature)

  def __lt__(self, other):
    from declafe import BiComposeFeature
    from declafe.binary import IsLessFeature

    return BiComposeFeature.make(self, self.__conv_const(other), IsLessFeature)

  def __ge__(self, other):
    from declafe import BiComposeFeature
    from declafe.binary import GEFeature

    return BiComposeFeature.make(self, self.__conv_const(other), GEFeature)

  def __le__(self, other):
    from declafe import BiComposeFeature
    from declafe.binary import LEFeature

    return BiComposeFeature.make(self, self.__conv_const(other), LEFeature)

  @staticmethod
  def sar(high: str, low: str) -> "FeatureGen":
    from declafe.binary import SARFeature
    return SARFeature(high, low)

  @staticmethod
  def sarext(high: str, low: str) -> "FeatureGen":
    from declafe.binary import SAREXTFeature
    return SAREXTFeature(high, low)

  @staticmethod
  def adxes(high: str, low: str, close: str, periods: List[int]) -> List["FeatureGen"]:
    return [FeatureGen.adx(high, low, close, period) for period in periods]

  @staticmethod
  def adx(high: str, low: str, close: str, period: int) -> "FeatureGen":
    from declafe.tri.ADXFeature import ADXFeature
    return ADXFeature(high, low, close, period)

  @staticmethod
  def adxrs(high: str, low: str, close: str, periods: List[int]) -> List["FeatureGen"]:
    return [FeatureGen.adx(high, low, close, period) for period in periods]

  @staticmethod
  def adxr(high: str, low: str, close: str, period: int) -> "FeatureGen":
    from declafe.tri import ADXRFeature
    return ADXRFeature(high, low, close, period)

  @staticmethod
  def aroon_up(high: str, low: str, period: int) -> "FeatureGen":
    from declafe.binary import AROONUpFeature
    return AROONUpFeature(high, low, period)

  @staticmethod
  def aroon_ups(high: str, low: str, periods: List[int]) -> List["FeatureGen"]:
    return [FeatureGen.aroon_up(high, low, period) for period in periods]

  @staticmethod
  def aroon_down(high: str, low: str, period: int) -> "FeatureGen":
    from declafe.binary import AROONDownFeature
    return AROONDownFeature(high, low, period)

  @staticmethod
  def aroon_downs(high: str, low: str, periods: List[int]) -> List["FeatureGen"]:
    return [FeatureGen.aroon_down(high, low, period) for period in periods]

  @staticmethod
  def arron_osc(high: str, low: str, period: int) -> "FeatureGen":
    from declafe.binary import AROONOSCFeature
    return AROONOSCFeature(high, low, period)

  @staticmethod
  def arron_oscs(high: str, low: str, periods: List[int]) -> List["FeatureGen"]:
    return [FeatureGen.arron_osc(high, low, period) for period in periods]

  @staticmethod
  def bop(open_col: str = "open", high: str = "high", low: str = "low", close: str = "close") -> "FeatureGen":
    from declafe.quadri import BOPFeature
    return BOPFeature(open_col, high, low, close)

  def __conv_const(self, con: Any):
    from declafe.dsl import c

    if not isinstance(con, FeatureGen):
      return c(con)
    else:
      return con

FG = FeatureGen
