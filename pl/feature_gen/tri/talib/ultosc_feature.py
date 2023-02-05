import polars as pl
from pl.feature_gen.types import ColLike
import talib
from pl.feature_gen.tri.tri_feature import TriFeature


class ULTOSCFeature(TriFeature):

  def __init__(self,
               col1: ColLike,
               col2: ColLike,
               col3: ColLike,
               timeperiod1: int = 7,
               timeperiod2: int = 14,
               timeperiod3: int = 28):
    super().__init__(col1, col2, col3)
    self.timeperiod1 = timeperiod1
    self.timeperiod2 = timeperiod2
    self.timeperiod3 = timeperiod3

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return pl.struct(
        [col1, col2,
         col3]).map(lambda s: talib.ULTOSC(s[f'{self.col1.feature_name}'],
                                           s[f'{self.col2.feature_name}'],
                                           s[f'{self.col3.feature_name}'],
                                           timeperiod1=self.timeperiod1,
                                           timeperiod2=self.timeperiod2,
                                           timeperiod3=self.timeperiod3))

  def _feature_names(self) -> list[str]:
    return [
        f'ULTOSC({self.timeperiod1}, {self.timeperiod2}, {self.timeperiod3})({self.col1}, {self.col2}, {self.col3})'
    ]
