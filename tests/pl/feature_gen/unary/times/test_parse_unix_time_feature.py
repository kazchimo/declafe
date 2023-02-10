import polars as pl
import declafe.pl.feature_gen as fg
from datetime import datetime


def test_parse_unixtime():
  df = pl.DataFrame({
      "a": [
          1612137600000000000,
          1612224000000000000,
          1612310400000000000,
          1612396800000000000,
      ]
  })
  parse_unixtime = fg.col("a").parse_unixtime("ns")
  assert parse_unixtime(df).series_equal(
      pl.Series(
          "parse_unixtime(a)",
          [
              datetime(2021, 2, 1, 0, 0),
              datetime(2021, 2, 2, 0, 0),
              datetime(2021, 2, 3, 0, 0),
              datetime(2021, 2, 4, 0, 0),
          ],
      ))

  df = pl.DataFrame({
      "a": [
          1612137600000000,
          1612224000000000,
          1612310400000000,
          1612396800000000,
      ]
  })
  parse_unixtime = fg.col("a").parse_unixtime("us")
  assert parse_unixtime(df).series_equal(
      pl.Series(
          "parse_unixtime(a)",
          [
              datetime(2021, 2, 1, 0, 0),
              datetime(2021, 2, 2, 0, 0),
              datetime(2021, 2, 3, 0, 0),
              datetime(2021, 2, 4, 0, 0),
          ],
      ))
