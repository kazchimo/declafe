from typing import List, Union, Callable

from pl.feature_gen.feature_gen import FeatureGen
import polars as pl


class Features:

  def __init__(self, feature_gens: List[FeatureGen]):
    super().__init__()

    fs: List["FeatureGen"] = []

    for fe in feature_gens:
      if all([not f.equals(fe) for f in fs]):
        fs.append(fe)

    self.feature_gens = fs

  def transform(
      self,
      temp_df: pl.DataFrame,
  ) -> pl.DataFrame:
    orig_columns = [
        pl.col(c) for c in temp_df.columns if c not in self.feature_names
    ]
    return temp_df.select(orig_columns + [f.expr() for f in self.feature_gens])

  def set_features(self, temp_df: pl.DataFrame) -> pl.DataFrame:
    return self.transform(temp_df)

  @property
  def feature_names(self) -> List[str]:
    return [f.feature_name for f in self.feature_gens]

  def map(self, func: Callable[["FeatureGen"], "FeatureGen"]) -> "Features":
    return Features([func(f) for f in self.feature_gens])

  def contains(self, feature: Union["FeatureGen", str]) -> bool:
    if isinstance(feature, str):
      return feature in self.feature_names
    else:
      return feature.feature_name in self.feature_names

  def add_feature(self, feature: "FeatureGen") -> "Features":
    if feature.feature_name in self.feature_names:
      return self
    else:
      return Features(self.feature_gens + [feature])

  def __call__(self, temp_df: pl.DataFrame) -> pl.DataFrame:
    return self.transform(temp_df)

  def __contains__(self, item: Union["FeatureGen", str]) -> bool:
    return self.contains(item)

  def __add__(self, other: "Features") -> "Features":
    return Features(self.feature_gens + other.feature_gens)

  def __radd__(self, other: "Features") -> "Features":
    return Features(other.feature_gens + self.feature_gens)

  def __eq__(self, other: "Features") -> bool:
    return self.feature_names == other.feature_names

  @staticmethod
  def one(f: FeatureGen) -> "Features":
    return Features([f])

  @staticmethod
  def many(*fs: FeatureGen) -> "Features":
    return Features(list(fs))
