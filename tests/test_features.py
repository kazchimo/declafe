import pandas as pd

from declafe import Features, col
from declafe.unary import SumFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})


class TestMap:

  def test_return_mapped_values(self):
    fs = Features.many(col("a"), col("b")).map(SumFeature, periods=2)
    df = test_df.copy()
    fs.set_features(df)

    assert df["sum_2_of_a"].equals(df["a"].rolling(2).sum())
    assert df["sum_2_of_b"].equals(df["b"].rolling(2).sum())
