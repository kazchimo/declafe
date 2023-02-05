import polars as pl
from pl.feature_gen.types import ColLike
import talib
from pl.feature_gen.unary.unary_feature import UnaryFeature


class PPOFeature(UnaryFeature):

  def __init__(self, column: ColLike, fastperiod: int, slowperiod: int,
               matype: int):
    super().__init__(column)
    self.fastperiod = fastperiod
    self.slowperiod = slowperiod
    self.matype = matype

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.PPO(s,
                                            fastperiod=self.fastperiod,
                                            slowperiod=self.slowperiod,
                                            matype=self.matype))

  def _feature_names(self) -> list[str]:
    return [
        f'PPO({self.fastperiod}, {self.slowperiod}, {self.matype})({self.column})'
    ]
