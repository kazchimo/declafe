import polars as pl
import declafe.pl.feature_gen as fg


class TestIdFeature:

  def test_id_feature(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    id = fg.col("a")
    assert df["a"].series_equal(id(df))
