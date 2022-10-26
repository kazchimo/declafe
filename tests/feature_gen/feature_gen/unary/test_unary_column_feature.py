import pandas as pd

from declafe import ColLike
from declafe.feature_gen.unary import UnaryFeature


class Mul2Feature(UnaryFeature):

  def __init__(self, column_name: ColLike):
    super().__init__(column_name)

  @property
  def name(self) -> str:
    return "mul2"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser * 2


class TestFeatureName:

  def test_name_as_is_for_str(self):
    feature = Mul2Feature("close")
    assert feature.feature_name == "mul2_of_close"

  def test_parentheses_name_for_feature_gen(self):
    feature = Mul2Feature(Mul2Feature("close"))
    assert feature.feature_name == "mul2_of_(mul2_of_close)"
