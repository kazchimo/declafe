from dataclasses import dataclass, field
from typing import List, Type
from lib.features.unary import *
from .feature_gen import FeatureGen
import pandas as pd

class ClsMixin:
  moving_average_cls = MovingAverage


@dataclass
class Features(ClsMixin):
  feature_gens: List[FeatureGen]
  pre_processes: List[FeatureGen] = field(default_factory=list)

  def set_features(self, temp_df: pd.DataFrame, drop_nan: bool = False) -> pd.DataFrame:
    for p in self.pre_processes:
      p.set_feature(temp_df)

    for feature_gen in self.feature_gens:
      feature_gen.set_feature(temp_df)

    if drop_nan:
      temp_df.dropna(inplace=True)

    return temp_df

  @property
  def feature_names(self) -> List[str]:
    return [f.feature_name for f in self.feature_gens]

  def unary_feature_name_of(self, column_name: str):
    return [f.feature_name for f in self.feature_gens if
            isinstance(f, UnaryColumnFeature) and f.column_name == column_name]

  def filter_by_name(self, feature_names: List[str]):
    return Features([f for f in self.feature_gens if f.feature_name in feature_names])

  def contains(self, feature: FeatureGen) -> bool:
    return feature.feature_name in self.feature_names

  def __add__(self, other):
    return Features(self.feature_gens + [f for f in other.feature_gens if f.feature_name not in self.feature_names])

  def add_feature(self, feature_gen: FeatureGen):
    return Features(self.feature_gens + [feature_gen], self.pre_processes)

  def add_features(self, feature_gens: List[FeatureGen]):
    return Features(self.feature_gens + feature_gens, self.pre_processes)

  def show_features(self) -> None:
    for f in self.feature_gens:
      print(f.feature_name)

  def filter_out(self, features: List["FeatureGen"]) -> "Features":
    return Features([f for f in self.feature_gens if not Features(features).contains(f)])

  def filter_out_gen(self, cls: Type[FeatureGen]):
    return Features([f for f in self.feature_gens if not isinstance(f, cls)])

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

F = Features
