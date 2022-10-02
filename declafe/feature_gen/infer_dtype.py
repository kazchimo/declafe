from typing import Optional

import numpy as np
import pandas as pd

from declafe.feature_gen.types import NumericDTypes


def infer_min_numeric_type(col: pd.Series) -> Optional[NumericDTypes]:
  numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

  col_type = col.dtypes

  dt: Optional[NumericDTypes] = None

  if col_type in numerics:
    c_min = col.min()
    c_max = col.max()

    if str(col_type)[:3] == 'int':
      if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
        dt = "int8"
      elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
        dt = "int16"
      elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
        dt = "int32"
      elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
        dt = "int64"
    else:
      if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
        dt = "float16"
      elif c_min > np.finfo(np.float32).min and c_max < np.finfo(
          np.float32).max:
        dt = "float32"
      else:
        dt = "float64"

  return dt
