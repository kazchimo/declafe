import declafe.pl.feature_gen as fg
import polars as pl


class TestConstFeature:

  def test_const_feature(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    const = fg.lit(1)
    assert pl.Series("1", [1]).series_equal(const(df))
