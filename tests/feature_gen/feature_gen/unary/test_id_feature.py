import pandas as pd

from declafe import col
from declafe.feature_gen.unary import IdFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")


class TestDipAgainst:

  def test_calc_dip(self):
    df = test_df.copy()
    f = a.dip_against("b", 10)
    result = f.gen(df)

    assert result.equals(df["a"] / df["b"].rolling(10).max() - 1)


class TestDipAgainsts:

  def test_calc_dips(self):
    df = test_df.copy()
    f = a.dip_againsts("b", [10, 20])
    result = f.set_features(df)

    assert result["dip_a_against_max10_of_b"].equals(df["a"] /
                                                     df["b"].rolling(10).max() -
                                                     1)
    assert result["dip_a_against_max20_of_b"].equals(df["a"] /
                                                     df["b"].rolling(20).max() -
                                                     1)


class TestRipAgainst:

  def test_calc_rip(self):
    df = test_df.copy()
    f = a.rip_against("b", 10)
    result = f.gen(df)
    pred = df["a"] / df["b"].rolling(10).min() - 1

    assert result.equals(pred)


class TestRipAgainsts:

  def test_calc_rips(self):
    df = test_df.copy()
    f = a.rip_againsts("b", [10, 20])
    result = f.set_features(df)

    assert result["rip_a_against_min10_of_b"].equals(df["a"] /
                                                     df["b"].rolling(10).min() -
                                                     1)
    assert result["rip_a_against_min20_of_b"].equals(df["a"] /
                                                     df["b"].rolling(20).min() -
                                                     1)


class TestMany:

  def test_create_many_features(self):
    df = test_df.copy()
    fs = IdFeature.many(["a", "b"])
    result = fs.set_features(df)

    assert result["a"].equals(df["a"])
    assert result["b"].equals(df["b"])
