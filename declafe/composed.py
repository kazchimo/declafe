from declafe import ComposedFeature
from declafe.binary import IsGreaterFeature
from declafe.binary.BiComposeFeature import BiComposeFeature
from declafe.binary.IsLessFeature import IsLessFeature
from declafe.unary import *


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
