from abc import ABC, abstractmethod

import pandas as pd

from declafe.feature_gen import FeatureGen


class UnaryColumnFeature(FeatureGen, ABC):

  def __init__(self, column_name: str):
    super().__init__()
    self.column_name = column_name

  @property
  @abstractmethod
  def name(self) -> str:
    """
    各featureクラスをインスタンス化したときにcolumn_nameを除外した名前
    e.g. PctChangeFeature(column_name="close", periods=5) => "pct_change_5"
    """
    raise NotImplementedError

  def _feature_name(self) -> str:
    return f"{self.name}_of_{self.column_name}"

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return self.gen_unary(df[self.column_name])

  @abstractmethod
  def gen_unary(self, ser: pd.Series) -> pd.Series:
    raise NotImplementedError
