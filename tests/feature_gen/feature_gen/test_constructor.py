import pandas as pd
import talib

from declafe import col, c, FeatureGen

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001)),
    "d": list(range(3001, 4001)),
})

a = col("a")
b = col("b")
d = col("d")
_1 = c(1)

class TestAdx:
  def test_construct_adx(self):
    df = test_df.copy()
    result = FeatureGen.adx("a", "b", "d", 3).gen(df)

    assert result.equals(talib.ADX(df["a"], df["b"], df["d"], 3))

class TestAdxes:
  def test_construct_adxes(self):
    df = test_df.copy()
    result = FeatureGen.adxes("a", "b", "d", [3, 5]).set_features(df)

    assert result["ADX_3_of_d"].equals(talib.ADX(df["a"], df["b"], df["d"], 3))
    assert result["ADX_5_of_d"].equals(talib.ADX(df["a"], df["b"], df["d"], 5))

