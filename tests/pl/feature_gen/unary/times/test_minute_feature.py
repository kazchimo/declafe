import polars as pl
import declafe.pl.feature_gen as fg


def test_minute_feature():
  df = pl.DataFrame({
      "a": [
          "2021-01-01 00:00:00",
          "2021-01-02 00:01:00",
          "2021-01-03 00:02:00",
          "2021-01-04 00:03:00",
      ]
  }).with_columns([
      pl.col("a").str.strptime(pl.Datetime,
                               "%Y-%m-%d %H:%M:%S").suffix("_datetime"),
  ])

  minute = fg.col("a_datetime").minute()
  assert minute(df).series_equal(pl.Series(
      "minute(a_datetime)",
      [0, 1, 2, 3],
  ))

  df = pl.DataFrame({
      "a": [
          1612141871000000000,
          1612232542000000000,
          1612323213000000000,
          1612413884000000000,
      ]
  })
  minute = fg.col("a").parse_unixtime("ns").minute()
  assert minute(df).series_equal(
      pl.Series(
          "minute(parse_unixtime(a))",
          [11, 22, 33, 44],
      ))

  df = pl.DataFrame({
      "a": [
          1612141871000000,
          1612232542000000,
          1612323213000000,
          1612413884000000,
      ]
  })
  minute = fg.col("a").parse_unixtime("us").minute()
  assert minute(df).series_equal(
      pl.Series(
          "minute(parse_unixtime(a))",
          [11, 22, 33, 44],
      ))
