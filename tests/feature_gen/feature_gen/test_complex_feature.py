import numpy as np
import pandas as pd

from declafe import col

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
    result = f._gen(df)

    assert np.array_equal(result, df["a"] / df["b"].rolling(10).max() - 1, True)


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
    result = f._gen(df)
    pred = df["a"] / df["b"].rolling(10).min() - 1

    assert np.array_equal(result, pred, True)


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
