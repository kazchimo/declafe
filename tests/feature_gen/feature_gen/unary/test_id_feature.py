import pandas as pd

from declafe import col
from declafe.feature_gen.unary import IdFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")


class TestMany:

  def test_create_many_features(self):
    df = test_df.copy()
    fs = IdFeature.many(["a", "b"])
    result = fs.set_features(df)

    assert result["a"].equals(df["a"])
    assert result["b"].equals(df["b"])
