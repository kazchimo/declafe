from typing import Type, Optional, List

from .AggFeatures import AggFeatures
from .agg_fun import *

__all__ = ["GroupBy", "groupby"]


class GroupBy:

  def __init__(self, by: str, aggs: Optional[List[Type[AggFun]]] = None):
    if aggs is None:
      aggs = []
    self.aggs = aggs
    self.by = by

  @property
  def count(self):
    return self.add_agg(CountAgg)

  @property
  def last(self):
    return self.add_agg(LastAgg)

  @property
  def max(self):
    return self.add_agg(MaxAgg)

  @property
  def min(self):
    return self.add_agg(MinAgg)

  @property
  def mean(self):
    return self.add_agg(MeanAgg)

  @property
  def nunique(self):
    return self.add_agg(NUniqueAgg)

  @property
  def std(self):
    return self.add_agg(StdAgg)

  def add_agg(self, agg: Type[AggFun]):
    return GroupBy(self.by, self.aggs + [agg])

  def target(self, target: str):
    return AggFeatures(
        by=self.by, agg_funs=[agg(target=target) for agg in self.aggs])

  def targets(self, *targets: str):
    return AggFeatures(
        by=self.by,
        agg_funs=[
            agg(target=target) for target in targets for agg in self.aggs
        ])


def groupby(by: str) -> GroupBy:
  return GroupBy(by)
