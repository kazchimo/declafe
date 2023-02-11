from typing import List, Union, Callable, Type, Iterable, TypeVar, Any

from declafe.pl.feature_gen.feature_gen import FeatureGen
import polars as pl
import functools

T = TypeVar("T")
Fun = Callable[[T], "FeatureGen"]
Ap = Callable[[Fun], "Features"]


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
    return temp_df.lazy().select(orig_columns +
                                 [f.expr()
                                  for f in self.feature_gens]).collect()

  def set_features(self, temp_df: pl.DataFrame) -> pl.DataFrame:
    return self.transform(temp_df)

  @property
  def feature_names(self) -> List[str]:
    return [f.feature_name for f in self.feature_gens]

  @property
  def feature_count(self) -> int:
    return len(self.feature_gens)

  def contains(self, feature: Union["FeatureGen", str]) -> bool:
    if isinstance(feature, str):
      return feature in self.feature_names
    else:
      return feature.feature_name in self.feature_names

  def extract(self, df: pl.DataFrame) -> pl.DataFrame:
    return df.select(self.feature_names)

  def add_feature(self, feature: "FeatureGen") -> "Features":
    if feature.feature_name in self.feature_names:
      return self
    else:
      return Features(self.feature_gens + [feature])

  def add_features(
      self, features: Union["Features", list["FeatureGen"]]) -> "Features":
    return self + features

  def filter_by_name(self, feature_names: List[str]) -> "Features":
    return Features(
        [f for f in self.feature_gens if f.feature_name in feature_names])

  def filter_not_by_name(self, feature_names: List[str]) -> "Features":
    return Features(
        [f for f in self.feature_gens if f.feature_name not in feature_names])

  def filter(self, func: Callable[["FeatureGen"], bool]) -> "Features":
    return Features([f for f in self.feature_gens if func(f)])

  def filter_not(self, func: Callable[["FeatureGen"], bool]) -> "Features":
    return self.filter(lambda f: not func(f))

  def filter_by_gen(self, cls: Type["FeatureGen"]) -> "Features":
    return Features([f for f in self.feature_gens if isinstance(f, cls)])

  def filter_not_by_gen(self, cls: Type["FeatureGen"]) -> "Features":
    return Features([f for f in self.feature_gens if not isinstance(f, cls)])

  def map(self, func: Callable[["FeatureGen"], "FeatureGen"]) -> "Features":
    return Features([func(f) for f in self.feature_gens])

  def map_aliases_with_idx(self, func: Callable[[int, str], str]) -> "Features":
    return Features([
        f.map_alias(lambda s: func(idx, s))
        for idx, f in enumerate(self.feature_gens)
    ])

  def map_aliases(self, func: Callable[[str], str]) -> "Features":
    return Features([f.map_alias(func) for f in self.feature_gens])

  def flat_map(
      self, fun: Callable[["FeatureGen"], Union["Features", list["FeatureGen"]]]
  ) -> "Features":
    return Features([f for fg in self.feature_gens for f in fun(fg)])

  def zip_with(
      self, fs: "Features", f: Callable[["FeatureGen", "FeatureGen"],
                                        "FeatureGen"]) -> "Features":
    return Features(
        [f(f1, f2) for f1, f2 in zip(self.feature_gens, fs.feature_gens)])

  def reduce(self, func: Callable[["FeatureGen", "FeatureGen"], "FeatureGen"],
             initial: Union["FeatureGen", Any]) -> "FeatureGen":
    from declafe.pl.feature_gen import conv_lit
    init = conv_lit(initial)
    return functools.reduce(func, self.feature_gens, init)

  def __call__(self, temp_df: pl.DataFrame) -> pl.DataFrame:
    return self.transform(temp_df)

  def __contains__(self, item: Union["FeatureGen", str]) -> bool:
    return self.contains(item)

  def __add__(self, other: Union["Features", list["FeatureGen"]]) -> "Features":
    if isinstance(other, Features):
      return Features(self.feature_gens + other.feature_gens)
    else:
      return Features(self.feature_gens + other)

  def __radd__(self, other: "Features") -> "Features":
    return Features(other.feature_gens + self.feature_gens)

  def __eq__(self, other: "Features") -> bool:
    return self.feature_names == other.feature_names

  def __len__(self) -> int:
    return self.feature_count

  def __iter__(self):

    return self.feature_gens.__iter__()

  @staticmethod
  def empty() -> "Features":
    return Features([])

  @staticmethod
  def one(f: FeatureGen) -> "Features":
    return Features([f])

  @staticmethod
  def many(*fs: FeatureGen) -> "Features":
    return Features(list(fs))

  @staticmethod
  def iter_over(it: Iterable[T]) -> Ap:

    def ap(f: Fun) -> "Features":
      return Features([f(x) for x in it])

    return ap

  @staticmethod
  def from_iter(it: Iterable[FeatureGen]) -> "Features":
    return Features(list(it))
