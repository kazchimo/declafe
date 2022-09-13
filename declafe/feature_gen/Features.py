from dataclasses import dataclass, field
from typing import List, Type, Callable
import functools


from declafe.feature_gen.unary import *

__all__ = ["Features", "F"]


@dataclass
class Features:
  feature_gens: List[FeatureGen]
  pre_processes: List[FeatureGen] = field(default_factory=list)

  def __post_init__(self):
    """
    Remove duplicated features and pre_processes
    """
    fs: List[FeatureGen] = []

    for fe in self.feature_gens:
      if all([not f.equals(fe) for f in fs]):
        fs.append(fe)

    ps: List[FeatureGen] = []

    for pre in self.pre_processes:
      if all([not p.equals(pre) for p in ps]):
        ps.append(pre)

    self.feature_gens = fs
    self.pre_processes = ps

  def set_features(self,
                   temp_df: pd.DataFrame,
                   drop_nan: bool = False) -> pd.DataFrame:
    df = temp_df
    for p in self.pre_processes:
      df = p.set_feature(df)

    for feature_gen in self.feature_gens:
      df = feature_gen.set_feature(df)

    if drop_nan:
      df.dropna(inplace=True)

    return df

  @property
  def feature_names(self) -> List[str]:
    return [f.feature_name for f in self.feature_gens]

  def unary_feature_name_of(self, column_name: str):
    return [
        f.feature_name
        for f in self.feature_gens
        if isinstance(f, UnaryColumnFeature) and f.column_name == column_name
    ]



  def contains(self, feature: FeatureGen) -> bool:
    return feature.feature_name in self.feature_names

  def __add__(self, other):
    return Features(self.feature_gens + [
        f for f in other.feature_gens
        if f.feature_name not in self.feature_names
    ])

  def add_feature(self, feature_gen: FeatureGen):
    return Features(self.feature_gens + [feature_gen], self.pre_processes)

  def add_features(self, feature_gens: List[FeatureGen]):
    return Features(self.feature_gens + feature_gens, self.pre_processes)

  def show_features(self) -> None:
    for f in self.feature_gens:
      print(f.feature_name)
  def filter_by_name(self, feature_names: List[str]):
    return Features(
        [f for f in self.feature_gens if f.feature_name in feature_names])

  def filter_not_by_name(self, feature_names: List[str]):
    return Features(
        [f for f in self.feature_gens if f.feature_name not in feature_names])

  def filter(self, feature: List[FeatureGen]):
    return Features([f for f in self.feature_gens if Features(feature).contains(f)])

  def filter_not(self, features: List["FeatureGen"]) -> "Features":
    return Features(
        [f for f in self.feature_gens if not Features(features).contains(f)])

  def filter_gen(self, cls: Type[FeatureGen]):
    return Features([f for f in self.feature_gens if isinstance(f, cls)])

  def filter_not_gen(self, cls: Type[FeatureGen]):
    return Features([f for f in self.feature_gens if not isinstance(f, cls)])

  def reduce(self, f: Callable[["FeatureGen", "FeatureGen"], "FeatureGen"], initial: "FeatureGen"):
    return functools.reduce(f, self.feature_gens, initial)

  def map(self, f: Type["UnaryColumnFeature"], **kwargs) -> "Features":
    return Features([fg.next(f, **kwargs) for fg in self.feature_gens])

  @property
  def feature_count(self) -> int:
    return len(self.feature_gens)

  @staticmethod
  def empty() -> "Features":
    return Features([])

  @staticmethod
  def one(feature_gen: FeatureGen) -> "Features":
    return Features([feature_gen])

  @staticmethod
  def two(feature_gen1: FeatureGen, feature_gen2: FeatureGen) -> "Features":
    return Features([feature_gen1, feature_gen2])

  @staticmethod
  def many(*args: FeatureGen) -> "Features":
    return Features(list(args))

  def __iter__(self):
    return self.feature_gens.__iter__()


F = Features
