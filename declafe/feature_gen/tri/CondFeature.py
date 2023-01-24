import numpy as np
import pandas as pd

from declafe import ColLike
from declafe.feature_gen.tri.TriFeature import TriFeature

__all__ = ["CondFeature"]


class CondFeature(TriFeature):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike):
    """
    :param col1: test column
    :param col2: true column
    :param col3: false column
    """
    super().__init__(col1, col2, col3)

  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    return pd.DataFrame({
        "test": col1,
        "true": col2,
        "false": col3
    }).apply(lambda x: x["true"]
             if x["test"] else x["false"], axis=1)  # type: ignore

  def _feature_name(self) -> str:
    return f"if_{self.col1}_then_{self.col2}_else_{self.col3}"
