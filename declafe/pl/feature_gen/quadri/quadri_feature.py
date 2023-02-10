from abc import ABC, abstractmethod

import polars as pl

from declafe.pl.feature_gen.feature_gen import FeatureGen
from declafe.pl.feature_gen.types import ColLike


class QuadriFeature(FeatureGen, ABC):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike,
               col4: ColLike):
    super().__init__()
    self.col1 = col1
    self.col2 = col2
    self.col3 = col3
    self.col4 = col4

  @abstractmethod
  def _quadri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr,
                   col4: pl.Expr):
    raise NotImplementedError()

  def _expr(self) -> pl.Expr:
    return self._quadri_expr(self.col1_feature.expr(), self.col2_feature.expr(),
                             self.col3_feature.expr(), self.col4_feature.expr())

  @property
  def col1_feature(self) -> FeatureGen:
    from declafe.pl.feature_gen import col_like_to_feature_gen
    return col_like_to_feature_gen(self.col1)

  @property
  def col2_feature(self) -> FeatureGen:
    from declafe.pl.feature_gen import col_like_to_feature_gen
    return col_like_to_feature_gen(self.col2)

  @property
  def col3_feature(self) -> FeatureGen:
    from declafe.pl.feature_gen import col_like_to_feature_gen
    return col_like_to_feature_gen(self.col3)

  @property
  def col4_feature(self) -> FeatureGen:
    from declafe.pl.feature_gen import col_like_to_feature_gen
    return col_like_to_feature_gen(self.col4)
