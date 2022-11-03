from datetime import datetime

import numpy as np

from ..UnaryFeature import UnaryFeature

__all__ = ["SecondFeature"]


class SecondFeature(UnaryFeature):

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    gen = np.frompyfunc(
        lambda x: datetime.utcfromtimestamp(x / 1000_000_000).second, 1, 1)
    return gen(ser).astype(np.int64)

  @property
  def name(self) -> str:
    return f"second"
