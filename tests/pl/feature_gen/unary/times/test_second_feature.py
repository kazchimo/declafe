import polars as pl
import declafe.pl.feature_gen as fg


def test_second_feature():
  df = pl.DataFrame({
      "a": [
          "2021-01-01 00:00:01",
          "2021-01-02 00:00:02",
          "2021-01-03 00:00:03",
          "2021-01-04 00:00:04",
      ]
  }).with_columns([
      pl.col("a").str.strptime(pl.Datetime,
                               "%Y-%m-%d %H:%M:%S").suffix("_datetime"),
  ])

  second = fg.col("a_datetime").second()
  assert second(df).series_equal(pl.Series(
      "second(a_datetime)",
      [1, 2, 3, 4],
  ))

  df = pl.DataFrame({
      "a": [
          1612137601000000000,
          1612224002000000000,
          1612310403000000000,
          1612396804000000000,
      ]
  })
  second = fg.col("a").parse_unixtime("ns").second()
  assert second(df).series_equal(
      pl.Series(
          "second(parse_unixtime(a))",
          [1, 2, 3, 4],
      ))
