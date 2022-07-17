import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["FlipBoolFeature"]


class FlipBoolFeature(UnaryColumnFeature):

  @property
  def name(self) -> str:
    return f"not"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    if not pd.api.types.is_bool_dtype(ser):
      raise ValueError("serはbool型である必要があります")

    return ~ser
