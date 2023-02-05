import polars as pl
from pl.feature_gen.types import ColLike
import talib
from pl.feature_gen.tri.tri_feature import TriFeature


class WILLRFeature(TriFeature):

  def __init__(self,
               col1: ColLike,
               col2: ColLike,
               col3: ColLike,
               timeperiod: int = 14):
    super().__init__(col1, col2, col3)
    self.timeperiod = timeperiod

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return pl.struct(
        [col1, col2,
         col3]).map(lambda s: talib.WILLR(s[f'{self.col1.feature_name}'],
                                          s[f'{self.col2.feature_name}'],
                                          s[f'{self.col3.feature_name}'],
                                          timeperiod=self.timeperiod))

  def _feature_names(self) -> list[str]:
    return [f'WILLR({self.timeperiod})({self.col1}, {self.col2}, {self.col3})']
