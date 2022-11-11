from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Type, Union, Literal, Callable, Any

import numpy as np
import pandas as pd

__all__ = ["FeatureGen", "ColLike"]

from numba import jit

from .ChainMixin import ChainMixin
from .ComplexFeatureMixin import ComplexFeatureMixin
from .ConstructorMixin import ConstructorMixin
from .OpsMixin import OpsMixin
from .infer_dtype import infer_min_numeric_type
from .types import DTypes

if TYPE_CHECKING:
  from declafe.feature_gen.Features import Features

ColLike = Union["FeatureGen", str]


class FeatureGen(ABC, ConstructorMixin, ChainMixin, OpsMixin,
                 ComplexFeatureMixin):

  def _self(self) -> "FeatureGen":
    return self

  def __init__(self):
    super().__init__()
    self.override_feature_name: Optional[str] = None
    self.dtype: Optional[Union[DTypes, Literal["numeric_auto"]]] = None
    self._enable_numba = False

  @abstractmethod
  def _gen(self, df: pd.DataFrame) -> np.ndarray:
    raise NotImplementedError

  def generate(self, df: pd.DataFrame) -> np.ndarray:
    """
    optimized gen
    """
    try:
      result = df[self.feature_name].to_numpy() \
        if self.feature_name in df.columns \
        else self._gen(df)

      dt = infer_min_numeric_type(result) \
        if self.dtype == "numeric_auto" \
        else self.dtype
    except Exception as e:
      raise Exception(f"Failed to generate {self.feature_name}") from e

    if dt == "category":
      dt = "int"

    assert len(df) == len(
        result
    ), f"len(df)={len(df)}, len(result)={len(result)}, feature_name={self.feature_name}"

    return result.astype(dt) if dt else result

  @abstractmethod
  def _feature_name(self) -> str:
    """
    default feature name used for this FeatureGen class
    """
    raise NotImplementedError

  @property
  def feature_name(self) -> str:
    return self.override_feature_name or \
           (self._feature_name())

  def equals(self, other: "FeatureGen") -> bool:
    return self.feature_name == other.feature_name

  @property
  def to_features(self) -> "Features":
    return self._FS.one(self)

  def combine(self, other: "FeatureGen") -> "Features":
    return self.to_features.add_feature(other)

  def as_name_of(self, feature_name: str) -> "FeatureGen":
    self.override_feature_name = feature_name
    return self

  def set_feature(self, df: pd.DataFrame) -> "pd.DataFrame":
    if self.feature_name in df.columns and df[
        self.feature_name].dtype == self.dtype:
      return df

    temp_df = df.drop(
        columns=[self.feature_name]) if self.feature_name in df.columns else df

    return pd.concat([
        temp_df,
        pd.DataFrame({self.feature_name: self.generate(df)}, index=df.index)
    ],
                     axis=1)

  def as_type(self, dtype: DTypes) -> "FeatureGen":
    self.dtype = dtype
    return self

  def as_bool(self) -> "FeatureGen":
    return self.as_type("bool")

  def as_type_auto_num(self, override: bool = False) -> "FeatureGen":
    if self.dtype is None or override:
      self.dtype = "numeric_auto"

    return self

  def con_aps(self, f: Callable[["FeatureGen"], "Features"]) -> "Features":
    return self.to_features + f(self)

  def con_ap(self, f: Callable[["FeatureGen"], "FeatureGen"]) -> "Features":
    return self.to_features.add_feature(f(self))

  def enable_numba(self) -> "FeatureGen":
    self._enable_numba = True
    return self

  def disable_numba(self) -> "FeatureGen":
    self._enable_numba = False
    return self

  @property
  def numba_enabled(self) -> bool:
    return self._enable_numba

  def numba_dec(self, func: Callable[..., Any]):
    f = jit(nopython=True)(func) if self.numba_enabled else func

    def wrapper(*args, **kwargs):
      return f(*args, **kwargs)

    return wrapper

  @staticmethod
  def FS() -> "Type[Features]":
    from declafe.feature_gen.Features import Features
    return Features

  @property
  def _FS(self) -> "Type[Features]":
    from declafe.feature_gen.Features import Features
    return Features

  def to_col(self, c: Union["FeatureGen", str]) -> str:
    if isinstance(c, FeatureGen):
      return c.feature_name
    else:
      return c

  def __str__(self):
    return self.feature_name
