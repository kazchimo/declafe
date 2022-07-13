from lib.features import ComposedFeature
from lib.features.binary import IsGreaterFeature
from lib.features.binary.BiComposeFeature import BiComposeFeature
from lib.features.binary.IsLessFeature import IsLessFeature
from lib.features.dsl import *
from lib.features.unary import *


def BreakoutBBandUpperFeature(price_column: str, bbands_column: str, bbands_periods: int) -> BiComposeFeature:
  return BiComposeFeature(
    IdFeature(price_column),
    BBandsUpperFeature(column_name=bbands_column, periods=bbands_periods),
    IsGreaterFeature
  )


def BreakoutBBandLowerFeature(price_column: str, bbands_column: str, bbands_periods: int) -> BiComposeFeature:
  return BiComposeFeature(
    IdFeature(price_column),
    BBandsLowerFeature(column_name=bbands_column, periods=bbands_periods),
    IsLessFeature
  )

def EMAOfPctChangeFeature(pct_change_column: str, pct_change_period: int, ema_period: int) -> ComposedFeature:
  return PctChangeFeature(column_name=pct_change_column, periods=pct_change_period).next(EMAFeature, periods=ema_period)

def DipFeature(price_column: str, high_column: str, hh_period: int) -> ComposedFeature:
  gen = (col(price_column) / col(high_column).moving_max(hh_period)) - c(1)
  return gen.as_name_of(f"dip_{price_column}_against_max{hh_period}_of_{high_column}")

def RipFeature(price_column: str, low_column: str, ll_period: int) -> ComposedFeature:
  gen = (col(price_column) / col(low_column).moving_min(ll_period)) - c(1)
  return gen.as_name_of(f"rip_{price_column}_against_min{ll_period}_of_{low_column}")

def MinuteNFeature(datetime_column: str, diviser: int):
  """区切りのいい分を表す"""
  gen = (col(datetime_column).minute() % c(diviser)) == c(0)
  return gen.as_name_of(f"minute{diviser}")

def HourNFeature(datetime_column: str, diviser: int):
  """区切りのいい時間を表す"""
  gen = (col(datetime_column).hour() % c(diviser)) == c(0)
  return gen.as_name_of(f"hour{diviser}")
