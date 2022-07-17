from abc import ABC, abstractmethod
from typing import Any

import pandas as pd

__all__ = ["AggFun"]

from declafe.feature_gen.unary import IdFeature


class AggFun(ABC):

  def __init__(self, target: str):
    self.target = target

  @abstractmethod
  def __call__(self, ser: pd.Series) -> Any:
    raise NotImplementedError

  @property
  @abstractmethod
  def fun_name(self) -> str:
    raise NotImplementedError

  @property
  def name(self) -> str:
    return f"{self.fun_name}_of_{self.target}"

  @property
  def as_id(self) -> "IdFeature":
    return IdFeature(self.name)

  def as_named_agg(self) -> pd.NamedAgg:
    return pd.NamedAgg(column=self.target, aggfunc=self)

  def __eq__(self, other) -> bool:
    return self.name == other.name

  def __hash__(self):
    return self.name.__hash__()
