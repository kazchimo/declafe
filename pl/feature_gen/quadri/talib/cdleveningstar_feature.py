import polars as pl
from pl.feature_gen.types import ColLike
import talib
from typing import cast

from pl.feature_gen.quadri.quadri_feature import QuadriFeature


class CDLEVENINGSTARFeature(QuadriFeature):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike, col4: ColLike,
               penetration: float):
    super().__init__(col1, col2, col3, col4)
    self.penetration = penetration

  def _quadri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr,
                   col4: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct(
        [col1, col2, col3, col4])).map(lambda s: talib.CDLEVENINGSTAR(
            s.apply(lambda ss: ss[f'{self.col1_feature.feature_name}']),
            s.apply(lambda ss: ss[f'{self.col2_feature.feature_name}']),
            s.apply(lambda ss: ss[f'{self.col3_feature.feature_name}']),
            s.apply(lambda ss: ss[f'{self.col4_feature.feature_name}']),
            penetration=self.penetration))

  def _feature_names(self) -> list[str]:
    return [
        f'CDLEVENINGSTAR({self.penetration})({self.col1}, {self.col2}, {self.col3}, {self.col4})'
    ]
