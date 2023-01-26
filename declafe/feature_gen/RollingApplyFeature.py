from typing import List, Optional, Protocol

import numpy as np
import pandas as pd

from .FeatureGen import FeatureGen, ColLike


class F(Protocol):

  def __call__(self, *args: np.ndarray) -> np.ndarray:
    ...


class RollingApplyFeature(FeatureGen):

  def __init__(self,
               target_col: ColLike,
               window: int,
               f: F,
               ops_name: str,
               additional_columns: Optional[List[ColLike]] = None):
    super().__init__()
    if additional_columns is None:
      additional_columns = []

    self.target_col = self.to_col_feature_gen(target_col)
    self.window = window
    self.f = f
    self.ops_name = ops_name
    self.additional_columns = [
        self.to_col_feature_gen(c) for c in additional_columns
    ]

  def _gen(self, df: pd.DataFrame) -> np.ndarray:

    def ap(arr: pd.Series, df: pd.DataFrame) -> np.ndarray:
      temp_df = df.loc[arr.index]
      others = [c(temp_df) for c in self.additional_columns]
      return self.f(arr.to_numpy(), *others)

    return pd.Series(self.target_col(df), index=df.index)\
      .rolling(window=self.window)\
      .apply(ap, raw=False, args=(df, )).to_numpy()

  def _feature_name(self) -> str:
    additional_column_names = [c.feature_name for c in self.additional_columns]
    additional_columns = "_" + "_".join(additional_column_names) \
      if len( self.additional_columns) > 0 \
      else ""
    return f"rolling_apply_{self.ops_name}_over_{self.target_col}{additional_columns}_{self.window}"
