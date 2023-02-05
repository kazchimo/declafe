import polars as pl
from pl.feature_gen.types import ColLike
import talib
from pl.feature_gen.quadri.quadri_feature import QuadriFeature


class CDLMORNINGSTARFeature(QuadriFeature):

  def __init__(self,
               col1: ColLike,
               col2: ColLike,
               col3: ColLike,
               col4: ColLike,
               penetration: float = 0):
    super().__init__(col1, col2, col3, col4)
    self.penetration = penetration

  def _quadri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr,
                   col4: pl.Expr) -> pl.Expr:
    return pl.struct([
        col1, col2, col3, col4
    ]).map(lambda s: talib.CDLMORNINGSTAR(s[f'{self.col1.feature_name}'],
                                          s[f'{self.col2.feature_name}'],
                                          s[f'{self.col3.feature_name}'],
                                          s[f'{self.col4.feature_name}'],
                                          penetration=self.penetration))

  def _feature_names(self) -> list[str]:
    return [
        f'CDLMORNINGSTAR({self.penetration})({self.col1}, {self.col2}, {self.col3}, {self.col4})'
    ]
