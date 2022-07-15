from typing import List, Dict

import pandas as pd

from .agg_fun import AggFun


class AggFeatures:

  def __init__(self, by: str, agg_funs: List[AggFun]):
    self.agg_funs = agg_funs
    self.by = by

  def gen(self, df: pd.DataFrame, reset_index: bool = True) -> pd.DataFrame:
    if reset_index:
      return df.groupby(self.by).agg(**self._named_agg_funs()).reset_index()
    else:
      return df.groupby(self.by).agg(**self._named_agg_funs())

  @property
  def agg_names(self):
    return [fun.name for fun in self.agg_funs]

  def _named_agg_funs(self) -> Dict[str, pd.NamedAgg]:
    return {fun.name: fun.as_named_agg() for fun in self.agg_funs}

  def __sub__(self, other):
    self.__check_same_by(other)
    return AggFeatures(
        self.by, [fun for fun in self.agg_funs if fun not in other.agg_funs])

  def __add__(self, other):
    self.__check_same_by(other)
    non_dup = other - self
    return AggFeatures(self.by, self.agg_funs + non_dup.agg_funs)

  def __eq__(self, other) -> bool:
    return self.by == other.by and self.agg_funs == other.agg_funs

  def __check_same_by(self, other: "AggFeatures") -> None:
    if self.by != other.by:
      raise ValueError("AggFeatures must be added with same by")
