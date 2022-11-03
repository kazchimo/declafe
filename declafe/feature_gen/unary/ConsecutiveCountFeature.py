from typing import Any

import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["ConsecutiveCountFeature"]


class ConsecutiveCountFeature(UnaryFeature):
  """対象値の連続数を返す"""

  def __init__(self, column_name: str, target_value: Any = 1):
    super().__init__(column_name)
    self.target_value = target_value

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    """see: https://stackoverflow.com/questions/27626542/counting-consecutive-positive-values-in-python-pandas-array"""
    condition = (ser == self.target_value)
    gen_arr = np.frompyfunc(lambda b: np.arange(b), 1, 1)
    res = gen_arr(np.bincount(np.cumsum(condition != np.roll(condition, 1))))

    return condition * (np.concatenate(res) + 1)

  @property
  def name(self) -> str:
    return f"consecutive_count_{self.target_value}"
