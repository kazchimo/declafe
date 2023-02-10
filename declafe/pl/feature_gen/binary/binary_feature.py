from abc import ABC, abstractmethod

import polars as pl

from declafe.pl.feature_gen.feature_gen import FeatureGen
from declafe.pl.feature_gen.types import ColLike


class BinaryFeature(FeatureGen, ABC):

  def __init__(self, left: ColLike, right: ColLike):
    super().__init__()
    self.left = left
    self.right = right

  @abstractmethod
  def _binary_expr(self, left: pl.Expr, right: pl.Expr):
    raise NotImplementedError()

  def _expr(self) -> pl.Expr:
    return self._binary_expr(self.left_feature.expr(),
                             self.right_feature.expr())

  @property
  def left_feature(self) -> FeatureGen:
    from declafe.pl.feature_gen import col_like_to_feature_gen
    return col_like_to_feature_gen(self.left)

  @property
  def right_feature(self) -> FeatureGen:
    from declafe.pl.feature_gen import col_like_to_feature_gen
    return col_like_to_feature_gen(self.right)

  @property
  def _left_wrapped_feature_name(self) -> str:
    return self.left_feature.wrapped_feature_name

  @property
  def _right_wrapped_feature_name(self) -> str:
    return self.right_feature.wrapped_feature_name
