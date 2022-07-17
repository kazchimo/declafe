import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["LagFeature"]


class LagFeature(UnaryColumnFeature):
  """
  ラグ特徴量を追加する
  過去のデータを使用することしか想定していない
  """

  def __init__(self, periods: int, column_name: str):
    super().__init__(column_name)
    self.periods = periods

    if self.periods <= 0:
      raise ValueError("periodsは正の整数である必要があります")

  @property
  def name(self) -> str:
    return f"lag_{self.periods}"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.shift(self.periods)
