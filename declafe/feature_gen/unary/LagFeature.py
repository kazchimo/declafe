import numpy as np

from .UnaryFeature import UnaryFeature

__all__ = ["LagFeature"]


class LagFeature(UnaryFeature):
  """
  ラグ特徴量を追加する
  過去のデータを使用することしか想定していない
  """

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

  @property
  def name(self) -> str:
    return f"lag_{self.periods}"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return np.where(
        np.arange(len(ser)) < self.periods, np.nan, np.roll(ser, self.periods))
