from typing import Union, Literal

import numpy as np

NumericDTypes = Union[Literal["int8"], Literal["int16"], Literal["int32"],
                      Literal["int64"], Literal["float16"], Literal["float32"],
                      Literal["float64"], Literal["uint8"], Literal["uint16"],
                      Literal["uint32"], Literal["uint64"]]

DTypes = Union[Literal["category"], Literal["bool"], Literal["datetime64[ns]"],
               Literal["timedelta[ns]"], Literal["object"], Literal["uint8"],
               Literal["uint16"], Literal["uint32"], Literal["uint64"],
               NumericDTypes]


def as_numeric(a: np.ndarray) -> np.ndarray:
  if np.issubdtype(a.dtype, np.number):
    return a
  else:
    return a.astype(np.float64)
