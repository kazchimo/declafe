import polars as pl
import pl.feature_gen as fg

a = fg.col("a")


class TestAbsFeature:

  def test_abs(self):
    df = pl.DataFrame({"a": [1, -2, 3]})
    abs_feature = a.abs()
    assert pl.Series("|a|", [1, 2, 3]).series_equal(abs_feature(df))

    f = a.abs().abs()
    assert pl.Series("||a||", [1, 2, 3]).series_equal(f(df))
