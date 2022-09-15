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

class TestAdd:
  def test_add(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert (col("a") + col("b")).gen(df).equals(pd.Series([5, 7, 9]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") + 1).gen(df).equals(pd.Series([2, 3, 4]))
