from typing import Callable

import pandas as pd

from declafe.feature_gen.unary import UnaryFeature


class FromFuncFeature(UnaryFeature):

  def __init__(self, column_name: str, func: Callable[[pd.Series], pd.Series],
               op_name: str):
    super().__init__(column_name)
    self.func = func
    self.op_name = op_name

  @property
  def name(self) -> str:
    return self.op_name

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return self.func(ser)
