from typing import List, Dict

import pandas as pd

from declafe.agg_feature_gen.agg_fun import AggFun


class AggFeatures:

  def __init__(self, by: str, agg_funs: List[AggFun]):
    self.agg_funs = agg_funs
    self.by = by

  def gen(self, df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(self.by).agg(**self._named_agg_funs())

  def _named_agg_funs(self) -> Dict[str, pd.NamedAgg]:
    return {fun.name: fun.as_named_agg() for fun in self.agg_funs}

  def __add__(self, other):
    if self.by != other.by:
      raise ValueError("AggFeatures must be added with same by")

    return AggFeatures(self.by, self.agg_funs + other.agg_funs)
