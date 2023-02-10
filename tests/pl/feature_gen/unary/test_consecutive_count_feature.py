import polars as pl
import pl.feature_gen as fg

a = fg.col("a")


class TestConsecutiveCount:

  def test_consecutive_count(self):
    df = pl.DataFrame({
        "a": [1, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "b": [1, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    })

    f = a.consecutive_count_of(1)

    assert f(df).series_equal(
        pl.Series(
            "consecutive_count_1_of_a",
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

  def test_consecutive_count_with_abs(self):
    df = pl.DataFrame({
        "a": [1, 2, 2, 2, 3, 3, 3, 3, 3, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1],
        "b": [1, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    })

    f = a.abs().consecutive_count_of(1)

    assert f(df).series_equal(
        pl.Series(
            "consecutive_count_1_of_(|a|)",
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
