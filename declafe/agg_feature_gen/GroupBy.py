import functools
from typing import Type, Optional, List, Protocol

from .AggFeatures import AggFeatures
from .agg_fun import *

__all__ = ["GroupBy", "groupby"]


class AggConst(Protocol):

  def __call__(self, target: str) -> AggFun:
    ...


def partialclass(cls, *args, **kwds):

  class NewCls(cls):  # type: ignore
    __init__ = functools.partialmethod(cls.__init__, *args, **kwds)

  return NewCls


class GroupBy:

  def __init__(self, by: str, aggs: Optional[List[AggConst]] = None):
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

  def diff_at(self, at: int):
    return self.add_agg(partialclass(DiffAtAgg, at=at))

  def add_agg(self, agg: Type[AggFun]):
    return GroupBy(self.by, self.aggs + [agg])

  def target(self, target: str):
    return AggFeatures(by=self.by,
                       agg_funs=[agg(target=target) for agg in self.aggs])

  def targets(self, *targets: str):
    return AggFeatures(
        by=self.by,
        agg_funs=[
            agg(target=target) for target in targets for agg in self.aggs
        ])


def groupby(by: str) -> GroupBy:
  return GroupBy(by)
