import polars as pl
from pl.feature_gen.types import ColLike
import talib
from typing import cast

from pl.feature_gen.binary.binary_feature import BinaryFeature


class SAREXTFeature(BinaryFeature):

  def __init__(self, left: ColLike, right: ColLike, startvalue: float,
               offsetonreverse: float, accelerationinitlong: float,
               accelerationlong: float, accelerationmaxlong: float,
               accelerationinitshort: float, accelerationshort: float,
               accelerationmaxshort: float):
    super().__init__(left, right)
    self.startvalue = startvalue
    self.offsetonreverse = offsetonreverse
    self.accelerationinitlong = accelerationinitlong
    self.accelerationlong = accelerationlong
    self.accelerationmaxlong = accelerationmaxlong
    self.accelerationinitshort = accelerationinitshort
    self.accelerationshort = accelerationshort
    self.accelerationmaxshort = accelerationmaxshort

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([left, right])).map(lambda s: talib.SAREXT(
        s.apply(lambda ss: ss[f'{self.left_feature.feature_name}']),
        s.apply(lambda ss: ss[f'{self.right_feature.feature_name}']),
        startvalue=self.startvalue,
        offsetonreverse=self.offsetonreverse,
        accelerationinitlong=self.accelerationinitlong,
        accelerationlong=self.accelerationlong,
        accelerationmaxlong=self.accelerationmaxlong,
        accelerationinitshort=self.accelerationinitshort,
        accelerationshort=self.accelerationshort,
        accelerationmaxshort=self.accelerationmaxshort))

  def _feature_names(self) -> list[str]:
    return [
        f'SAREXT({self.startvalue}, {self.offsetonreverse}, {self.accelerationinitlong}, {self.accelerationlong}, {self.accelerationmaxlong}, {self.accelerationinitshort}, {self.accelerationshort}, {self.accelerationmaxshort})({self.left}, {self.right})'
    ]
