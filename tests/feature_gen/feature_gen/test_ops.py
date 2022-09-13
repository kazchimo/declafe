import pandas as pd

from declafe import col

test_df = pd.DataFrame({
  "b1": [True, False, True, False],
  "b2": [True, True, False, False],
})

b1 = col("b1")
b2 = col("b2")

class TestAnd:
  def test_and(self):
    assert (b1 & b2).gen(test_df).equals(pd.Series([True, False, False, False]))

class TestOr:
  def test_or(self):
    assert (b1 | b2).gen(test_df).equals(pd.Series([True, True, True, False]))
