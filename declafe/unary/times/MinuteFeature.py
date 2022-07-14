import pandas as pd

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["MinuteFeature"]


class MinuteFeature(UnaryColumnFeature):
  """対象カラムの分を抜き出す"""

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: x.minute)

  @property
  def name(self) -> str:
    return f"minute"
