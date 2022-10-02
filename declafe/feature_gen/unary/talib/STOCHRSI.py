import pandas as pd
import talib

from declafe import ColLike
from declafe.feature_gen.unary import UnaryColumnFeature


class STOCHRSIFastkFeature(UnaryColumnFeature):

  def __init__(self,
               column_name: ColLike,
               period: int,
               fastk_period: int,
               fastd_period: int,
               fastd_matype: int = 0):
    super().__init__(column_name)
    self.period = period
    self.fastk_period = fastk_period
    self.fastd_period = fastd_period
    self.fastd_matype = fastd_matype

  @property
  def name(self) -> str:
    return f"STOCHRSI_fastk_{self.period}_{self.fastk_period}_{self.fastd_period}_{self.fastd_matype}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.STOCHRSI(ser,
                          timeperiod=self.period,
                          fastk_period=self.fastk_period,
                          fastd_period=self.fastd_period,
                          fastd_matype=self.fastd_matype)[0]


class STOCHRSIFastdFeature(UnaryColumnFeature):

  def __init__(self,
               column_name: ColLike,
               period: int,
               fastk_period: int,
               fastd_period: int,
               fastd_matype: int = 0):
    super().__init__(column_name)
    self.period = period
    self.fastk_period = fastk_period
    self.fastd_period = fastd_period
    self.fastd_matype = fastd_matype

  @property
  def name(self) -> str:
    return f"STOCHRSI_fastd_{self.period}_{self.fastk_period}_{self.fastd_period}_{self.fastd_matype}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.STOCHRSI(ser,
                          timeperiod=self.period,
                          fastk_period=self.fastk_period,
                          fastd_period=self.fastd_period,
                          fastd_matype=self.fastd_matype)[1]
