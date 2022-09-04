import pandas as pd

from declafe import col

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")

class TestMinComp:
  def test_return_min_value(self):
    df = test_df.copy()
    result = a.min_comp(500).gen(df)
    pred = pd.Series(list(range(1, 501)) + [500] * 500)

    assert result.equals(pred)


class TestMaxComp:
  def test_return_max_value(self):
    df = test_df.copy()
    result = a.max_comp(500).gen(df)
    pred = pd.Series([500] * 500 + list(range(501, 1001)))

    assert result.equals(pred)
