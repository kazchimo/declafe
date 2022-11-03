import numpy as np
import pandas as pd

from declafe import ColLike
from declafe.feature_gen.tri.TriFeature import TriFeature

__all__ = ["CondFeature"]


class CondFeature(TriFeature):

  def __init__(self, test_col: ColLike, true_col: ColLike, false_col: ColLike):
    super().__init__(test_col, true_col, false_col)

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
