import polars as pl
import declafe.pl.feature_gen as fg


class TestInvertFeature:

  def test_invert_feature(self):
    df = pl.DataFrame({"a": [True, False, True], "b": [False, True, False]})
    fa = ~fg.col("a")
    fb = ~fg.col("b")

    assert fa(df).series_equal(pl.Series("~a", [False, True, False]))
    assert fb(df).series_equal(pl.Series("~b", [True, False, True]))
