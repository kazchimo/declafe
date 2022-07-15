from abc import ABC, abstractmethod

import pandas as pd

__all__ = ["AsType"]


class AsType(ABC):

  @abstractmethod
  def set_type(self, df: pd.DataFrame) -> None:
    raise NotImplementedError()
