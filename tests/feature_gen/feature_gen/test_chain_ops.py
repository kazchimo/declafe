from datetime import datetime

import numpy as np
import pandas as pd
import talib

from declafe import col, c, FeatureGen, Features
from declafe.feature_gen.unary import LogFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")
_1 = c(1)


class TestCond:

  def test_cond(self):
    df = pd.DataFrame({
        "cond": [True, False],
        "a": [1, 2],
        "b": [3, 4],
    })
    f = col("cond").of_cond(col("a"), col("b"))

    assert f.generate(df).equals(pd.Series([1, 4]))


class TestThen:

  def test_thena(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5]})
    f = Features.many(
        a.then(lambda s: s + 1, "plus_one"),
        a.then(lambda s: pd.Series(s).rolling(2).max(), "max_rolling"),
    )

    result = f.set_features(df)

    assert result["plus_one_of_a"].equals(pd.Series([2, 3, 4, 5, 6]))
    assert result["max_rolling_of_a"].equals(pd.Series([np.nan, 2, 3, 4, 5]))


class TestAccumulate:

  def test_accumulate(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    f = a.accumulate("sum", lambda x, y: x + y)
    f2 = a.accumulate("find_latest_three", lambda x, y: y if y % 3 == 0 else x)

    print(f.generate(df))
    print(f2.generate(df))

    assert np.array_equal(f.generate(df), pd.Series([1, 3, 6, 10, 15, 21]))
    assert np.array_equal(f2.generate(df), pd.Series([1, 1, 3, 3, 3, 6]))


class TestExistWithin:

  def test_exist_within(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    f = a.exist_within(3, 3)

    assert np.array_equal(
        f.generate(df),
        pd.Series([False, False, True, True, True, False]),
    )


class TestMinComp:

  def test_return_min_value(self):
    df = test_df.copy()
    result = a.min_comp(500)._gen(df)
    pred = pd.Series(list(range(1, 501)) + [500] * 500)

    assert np.array_equal(result, pred)


class TestMaxComp:

  def test_return_max_value(self):
    df = test_df.copy()
    result = a.max_comp(500)._gen(df)
    pred = pd.Series([500] * 500 + list(range(501, 1001)))

    assert np.array_equal(result, pred, True)


class Double(FeatureGen):

  def __init__(self, column: str):
    super().__init__()
    self.column = column

  def _gen(self, df: pd.DataFrame) -> pd.Series:
    return df[self.column] * 2

  def _feature_name(self) -> str:
    return "double"


class TestLog:

  def test_return_log(self):
    assert np.array_equal(
        _1.log()._gen(test_df),
        LogFeature("").gen_unary(pd.Series(1, index=test_df.index)))
    assert np.array_equal(
        Double("a").log()._gen(test_df),
        LogFeature("").gen_unary(test_df["a"] * 2))


class TestMovingAverage:

  def test_return_moving_average(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})

    assert np.array_equal(
        a.moving_average(3)._gen(df), pd.Series([np.nan, np.nan, 2, 3, 4, 5]),
        True)


class TestMovingAverages:

  def test_return_moving_averages(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.moving_averages([2, 3]).set_features(df)

    assert np.array_equal(df["sma_2_of_a"],
                          pd.Series([np.nan, 1.5, 2.5, 3.5, 4.5, 5.5]), True)
    assert np.array_equal(df["sma_3_of_a"],
                          pd.Series([np.nan, np.nan, 2, 3, 4, 5]), True)


class TestMovingSum:

  def test_return_moving_sum(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    assert np.array_equal(
        a.moving_sum(3)._gen(df), pd.Series([np.nan, np.nan, 6, 9, 12, 15]),
        True)


class TestMovingSums:

  def test_return_moving_sums(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.moving_sums([2, 3]).set_features(df)

    assert df["sum_2_of_a"].equals(pd.Series([np.nan, 3, 5, 7, 9, 11]))
    assert df["sum_3_of_a"].equals(pd.Series([np.nan, np.nan, 6, 9, 12, 15]))


class TestEma:

  def test_return_ema(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    assert np.array_equal(a.ema(3).generate(df), talib.EMA(df["a"], 3), True)


class TestEmas:

  def test_return_emas(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.emas([2, 3]).set_features(df)

    assert df["EMA_2_of_a"].equals(pd.Series(talib.EMA(df["a"], 2)))
    assert df["EMA_3_of_a"].equals(pd.Series(talib.EMA(df["a"], 3)))


class TestDema:

  def test_return_dema(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    assert np.array_equal(a.dema(3).generate(df), talib.DEMA(df["a"], 3), True)


class TestDemas:

  def test_return_demas(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.demas([2, 3]).set_features(df)

    assert df["DEMA_2_of_a"].equals(pd.Series(talib.DEMA(df["a"], 2)))
    assert df["DEMA_3_of_a"].equals(pd.Series(talib.DEMA(df["a"], 3)))


class TestCmo:

  def test_return_cmo(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    assert np.array_equal(a.cmo(3).generate(df), talib.CMO(df["a"], 3), True)


class TestCmos:

  def test_return_cmos(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.cmos([2, 3]).set_features(df)

    assert df["CMO_2_of_a"].equals(pd.Series(talib.CMO(df["a"], 2)))
    assert df["CMO_3_of_a"].equals(pd.Series(talib.CMO(df["a"], 3)))


class TestWma:

  def test_return_wma(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    assert np.array_equal(a.wma(3).generate(df), talib.WMA(df["a"], 3), True)


class TestWmas:

  def test_return_wmas(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.wmas([2, 3]).set_features(df)

    assert df["wma_2_of_a"].equals(pd.Series(talib.WMA(df["a"], 2)))
    assert df["wma_3_of_a"].equals(pd.Series(talib.WMA(df["a"], 3)))


class TestKama:

  def test_return_kama(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    assert np.array_equal(a.kama(3).generate(df), talib.KAMA(df["a"], 3), True)


class TestKamas:

  def test_return_kamas(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.kamas([2, 3]).set_features(df)

    assert df["kama_2_of_a"].equals(pd.Series(talib.KAMA(df["a"], 2)))
    assert df["kama_3_of_a"].equals(pd.Series(talib.KAMA(df["a"], 3)))


class TestMama:

  def test_return_mama(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.mama().to_features.set_features(df)

    assert df["mama0.5-0.05_of_a"].equals(pd.Series(talib.MAMA(df["a"])[0]))


class TestFama:

  def test_return_fama(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.fama().to_features.set_features(df)

    assert df["fama0.5-0.05_of_a"].equals(pd.Series(talib.MAMA(df["a"])[1]))


class TestTema:

  def test_return_tema(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    assert np.array_equal(a.tema(3).generate(df), talib.TEMA(df["a"], 3), True)


class TestTemas:

  def test_return_temas(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.temas([2, 3]).set_features(df)

    assert df["TEMA_2_of_a"].equals(pd.Series(talib.TEMA(df["a"], 2)))
    assert df["TEMA_3_of_a"].equals(pd.Series(talib.TEMA(df["a"], 3)))


class TestTrima:

  def test_return_trima(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    assert np.array_equal(
        a.trima(3).generate(df), talib.TRIMA(df["a"], 3), True)


class TestTrimas:

  def test_return_trimas(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.trimas([2, 3]).set_features(df)

    assert df["TRIMA_2_of_a"].equals(pd.Series(talib.TRIMA(df["a"], 2)))
    assert df["TRIMA_3_of_a"].equals(pd.Series(talib.TRIMA(df["a"], 3)))


class TestT3:

  def test_return_t3(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    assert np.array_equal(a.t3(3).generate(df), talib.T3(df["a"], 3), True)


class TestT3s:

  def test_return_t3s(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.t3s([2, 3]).set_features(df)

    assert df["T3_2_of_a"].equals(pd.Series(talib.T3(df["a"], 2)))
    assert df["T3_3_of_a"].equals(pd.Series(talib.T3(df["a"], 3)))


class TestMovingMidpoint:

  def test_return_moving_midpoint(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    assert np.array_equal(
        a.moving_midpoint(3).generate(df), talib.MIDPOINT(df["a"], 3), True)


class TestPctChange:

  def test_return_pct_change(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})

    assert np.array_equal(
        a.pct_change(3).generate(df), [np.nan, np.nan, np.nan, 3.0, 1.5, 1.0],
        True)


class TestPctChanges:

  def test_return_pct_changes(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.pct_changes([2, 3]).set_features(df)

    assert df["pct_change_2_of_a"].equals(
        pd.Series([
            np.nan,
            np.nan,
            2.0,
            1.0,
            0.6666666666666667,
            0.5,
        ]))
    assert df["pct_change_3_of_a"].equals(
        pd.Series([np.nan, np.nan, np.nan, 3.0, 1.5, 1.0]))


class TestMovingMax:

  def test_return_moving_max(self):
    f = a.moving_max(3)
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

    assert np.array_equal(f._gen(df),
                          np.array([np.nan, np.nan, 3, 4, 5, 6, 7, 8, 9, 10]),
                          True)


class TestMovingMaxes:

  def test_return_moving_maxes(self):
    f = a.moving_maxes([2, 3])
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    df = f.set_features(df)

    assert df["max_2_of_a"].equals(
        pd.Series([np.nan, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert df["max_3_of_a"].equals(
        pd.Series([np.nan, np.nan, 3, 4, 5, 6, 7, 8, 9, 10]))


class TestMovingMin:

  def test_return_moving_min(self):
    f = a.moving_min(3)
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

    assert np.array_equal(f._gen(df),
                          np.array([np.nan, np.nan, 1, 2, 3, 4, 5, 6, 7, 8]),
                          True)


class TestMovingMins:

  def test_return_moving_mins(self):
    f = a.moving_mins([2, 3])
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    df = f.set_features(df)

    assert df["min_2_of_a"].equals(
        pd.Series([np.nan, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert df["min_3_of_a"].equals(
        pd.Series([np.nan, np.nan, 1, 2, 3, 4, 5, 6, 7, 8]))


class TestIsPositive:

  def test_return_is_positive(self):
    f = a.is_positive()
    df = pd.DataFrame({"a": [-1, 0, 1, 2, -2]})
    result = f.generate(df)

    assert np.array_equal(result, pd.Series([False, False, True, True, False]))


class TestRoundN:

  def test_return_round_n(self):
    f = a.round_n(2)
    df = pd.DataFrame({"a": [1.234, 2.345, 3.456]})
    result = f.generate(df)

    assert np.array_equal(result, pd.Series([1.23, 2.35, 3.46]))


class TestAdd:

  def test_add(self):
    assert np.array_equal((a + 1)._gen(test_df), test_df["a"] + 1)


class TestApo:

  def test_calc_apo(self):
    assert np.array_equal(
        a.apo(12, 26)._gen(test_df), talib.APO(test_df["a"], 12, 26), True)


class TestInvert:

  def test_invert(self):
    assert np.array_equal((~a)._gen(pd.DataFrame({"a": [True, False]})),
                          pd.Series([False, True]), True)

  def test_handle_float(self):
    assert np.array_equal((~a)._gen(pd.DataFrame({"a": [1.0, 0.0]})),
                          pd.Series([0.0, 1.0]), True)


class TestLag:

  def test_lag(self):
    assert np.array_equal(a.lag(1).generate(test_df),
                          test_df["a"].shift(1).values,
                          equal_nan=True)


class TestLags:

  def test_lags(self):
    df = a.lags([1, 2]).set_features(test_df)
    assert df["lag_1_of_a"].equals(test_df["a"].shift(1))
    assert df["lag_2_of_a"].equals(test_df["a"].shift(2))


class TestReplace:

  def test_replace(self):
    gen = a.lag(1).replace(np.nan, 99999)
    assert list(gen._gen(test_df)) == [99999] + list(range(1, 1000))


class TestReplaceNa:

  def test_replace_na(self):
    gen = a.lag(1).replace_na(99999)
    assert list(gen._gen(test_df)) == [99999] + list(range(1, 1000))


class TestConsecutiveCountOf:

  def test_calc_consecutive_count(self):
    df = pd.DataFrame({"a": ["a", "b", "b", "c", "b", "b", "b", "a", "b"]})
    gen = a.consecutive_count_of("b")

    assert np.array_equal(gen._gen(df), pd.Series([0, 1, 2, 0, 1, 2, 3, 0, 1]),
                          True)


class TestConsecutiveUpCount:

  def test_calc_consecutive_up_count(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]})
    gen = a.consecutive_up_count()

    assert np.array_equal(gen._gen(df),
                          pd.Series([0, 1, 2, 3, 4, 0, 0, 0, 0, 1]))


class TestConsecutiveDownCount:

  def test_calc_consecutive_down_count(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]})
    gen = a.consecutive_down_count()

    assert np.array_equal(gen._gen(df),
                          pd.Series([0, 0, 0, 0, 0, 1, 2, 3, 4, 0]))


class TestAbs:

  def test_abs(self):
    assert np.array_equal(
        a.abs()._gen(pd.DataFrame({"a": [-1, -2, -3, 4, 5, 6]})),
        pd.Series([1, 2, 3, 4, 5, 6]), True)


class TestIsUp:

  def test_is_up(self):
    assert np.array_equal(
        a.is_up()._gen(pd.DataFrame({"a": [-1, -2, -3, 4, 5, 6]})),
        pd.Series([False, False, False, True, True, True]), True)


class TestIsDown:

  def test_is_down(self):
    assert np.array_equal(
        a.is_down()._gen(pd.DataFrame({"a": [-1, -2, -3, 4, 5, 6]})),
        pd.Series([False, True, True, False, False, False]), True)


class TestMovingStd:

  def test_moving_std(self):
    res = a.moving_std(3)._gen(pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]}))

    print(res)

    assert np.array_equal(res, [
        np.nan, np.nan, 0.816496580927726, 0.816496580927726, 0.816496580927726,
        0.816496580927726
    ], True)


class TestMovingStds:

  def test_moving_stds(self):
    res = a.moving_stds([3, 5
                        ]).set_features(pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]}))

    assert np.array_equal(res["std_3_of_a"], [
        np.nan, np.nan, 0.816496580927726, 0.816496580927726, 0.816496580927726,
        0.816496580927726
    ], True)
    assert np.array_equal(res["std_5_of_a"], [
        np.nan, np.nan, np.nan, np.nan, 1.4142135623730951, 1.4142135623730951
    ], True)


class TestMACD:

  def test_calc_macd(self):
    assert np.array_equal(
        a.macd(12, 26, 9)._gen(test_df),
        talib.MACD(test_df["a"], 12, 26, 9)[0], True)


class TestMACDSignal:

  def test_calc_macd_signal(self):
    assert np.array_equal(
        a.macd_signal(12, 26, 9)._gen(test_df),
        talib.MACD(test_df["a"], 12, 26, 9)[1], True)


class TestMACDHist:

  def test_calc_macd_hist(self):
    assert np.array_equal(
        a.macd_hist(12, 26, 9)._gen(test_df),
        talib.MACD(test_df["a"], 12, 26, 9)[2], True)


class TestMOM:

  def test_calc_mom(self):
    assert np.array_equal(
        a.mom(10)._gen(test_df), talib.MOM(test_df["a"], 10), True)


class TestMOMS:

  def test_calc_moms(self):
    result = a.moms([10, 20]).set_features(test_df)

    assert result["MOM_10_of_a"].equals(talib.MOM(test_df["a"], 10))
    assert result["MOM_20_of_a"].equals(talib.MOM(test_df["a"], 20))


class TestRSI:

  def test_calc_rsi(self):
    assert np.array_equal(
        a.rsi(10)._gen(test_df), talib.RSI(test_df["a"], 10), True)


class TestRSIs:

  def test_calc_rsis(self):
    result = a.rsis([10, 20]).set_features(test_df)

    assert result["RSI_10_of_a"].equals(talib.RSI(test_df["a"], 10))
    assert result["RSI_20_of_a"].equals(talib.RSI(test_df["a"], 20))


class TestPPO:

  def test_calc_ppo(self):
    assert np.array_equal(
        a.ppo(26, 9)._gen(test_df), talib.PPO(test_df["a"], 26, 9), True)


class TestMaxWith:

  def test_max_with(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").max_with("b")._gen(df)

    assert np.array_equal(result, pd.Series([1, 2, 4]))

  def test_accept_feature_gen(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").max_with(col("b"))._gen(df)

    assert np.array_equal(result, pd.Series([1, 2, 4]), True)

  def test_dtype(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").max_with("b")._gen(df)
    assert result.dtype == int

    df = pd.DataFrame({"c1": [1.0, 2.0, 3.0], "b": [0.0, 1.0, 4.0]})
    result = col("c1").max_with("b")._gen(df)
    assert result.dtype == float

    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0.0, 1.0, 4.0]}).astype(object)
    result = col("c1").max_with("b")._gen(df)
    assert result.dtype == float


class TestMinWith:

  def test_min_with(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").min_with("b")._gen(df)

    assert np.array_equal(result, pd.Series([0, 1, 3]))

  def test_accept_feature_gen(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").min_with(col("b"))._gen(df)

    assert np.array_equal(result, pd.Series([0, 1, 3]), True)

  def test_dtype(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").min_with("b")._gen(df)
    assert result.dtype == int

    df = pd.DataFrame({"c1": [1.0, 2.0, 3.0], "b": [0.0, 1.0, 4.0]})
    result = col("c1").min_with("b")._gen(df)
    assert result.dtype == float

    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0.0, 1.0, 4.0]}).astype(object)
    result = col("c1").min_with("b")._gen(df)
    assert result.dtype == float


class TestBbandsUpper:

  def test_calc_bbands_upper(self):
    assert np.array_equal(
        a.bbands_upper(5, 2)._gen(test_df),
        (talib.BBANDS(test_df["a"], 5, 2)[0]), True)


class TestBbandsUppers:

  def test_calc_bbands_uppers(self):
    result = a.bbands_uppers([5, 10], 2).set_features(test_df)

    assert result["bbands_upper2_5_of_a"].equals(
        talib.BBANDS(test_df["a"], 5, 2)[0])
    assert result["bbands_upper2_10_of_a"].equals(
        talib.BBANDS(test_df["a"], 10, 2)[0])


class TestBBandsLower:

  def test_calc_bbands_lower(self):
    assert np.array_equal(
        a.bbands_lower(5, 2)._gen(test_df),
        talib.BBANDS(test_df["a"], 5, 2)[2], True)


class TestBBandsLowers:

  def test_calc_bbands_lowers(self):
    result = a.bbands_lowers([5, 10], 2).set_features(test_df)

    assert result["bbands_lower2_5_of_a"].equals(
        talib.BBANDS(test_df["a"], 5, 2)[2])
    assert result["bbands_lower2_10_of_a"].equals(
        talib.BBANDS(test_df["a"], 10, 2)[2])


class TestSTOCHRSIFastk:

  def test_calc_stochrsi_fastk(self):
    assert np.array_equal(
        a.stochrsi_fastk(10, 5, 3)._gen(test_df),
        (talib.STOCHRSI(test_df["a"], 10, 5, 3)[0]), True)


class TestSTOCHRSIFastks:

  def test_calc_stochrsi_fastks(self):
    result = a.stochrsi_fastks([10, 20], 5, 3).set_features(test_df)

    assert result["STOCHRSI_fastk_10_5_3_0_of_a"].equals(
        talib.STOCHRSI(test_df["a"], 10, 5, 3)[0])
    assert result["STOCHRSI_fastk_20_5_3_0_of_a"].equals(
        talib.STOCHRSI(test_df["a"], 20, 5, 3)[0])


class STOCHRSIFastd:

  def test_calc_stochrsi_fastd(self):
    assert a.stochrsi_fastd(10, 5, 3)\
      ._gen(test_df)\
      .equals(talib.STOCHRSI(test_df["a"], 10, 5, 3)[1])


class STOCHRSIFastds:

  def test_calc_stochrsi_fastds(self):
    result = a.stochrsi_fastds([10, 20], 5, 3).set_features(test_df)

    assert result["STOCHRSI_fastd_10_5_3_0_of_a"].equals(
        talib.STOCHRSI(test_df["a"], 10, 5, 3)[1])
    assert result["STOCHRSI_fastd_20_5_3_0_of_a"].equals(
        talib.STOCHRSI(test_df["a"], 20, 5, 3)[1])


class TestTRIX:

  def test_calc_trix(self):
    assert np.array_equal(
        a.trix(10)._gen(test_df), (talib.TRIX(test_df["a"], 10)), True)


class TestTRIXes:

  def test_calc_trixes(self):
    result = a.trixes([10, 20]).set_features(test_df)

    assert result["TRIX_10_of_a"].equals(talib.TRIX(test_df["a"], 10))
    assert result["TRIX_20_of_a"].equals(talib.TRIX(test_df["a"], 20))


class TestHT_DCPERIOD:

  def test_calc_ht_dcp(self):
    assert np.array_equal(a.ht_dcperiod()._gen(test_df),
                          (talib.HT_DCPERIOD(test_df["a"])), True)


class TestHT_DCPHASE:

  def test_calc_ht_dcp(self):
    assert np.array_equal(a.ht_dcphase()._gen(test_df),
                          (talib.HT_DCPHASE(test_df["a"])), True)


class TestHTPhasorInphase:

  def test_calc_ht_phasor_inphase(self):
    assert np.array_equal(a.ht_phasor_inphase()._gen(test_df),
                          (talib.HT_PHASOR(test_df["a"])[0]), True)


class TestHTPhasorQuadrature:

  def test_calc_ht_phasor_quadrature(self):
    assert np.array_equal(a.ht_phasor_quadrature()._gen(test_df),
                          (talib.HT_PHASOR(test_df["a"])[1]), True)


class TestHTSine:

  def test_calc_ht_sine(self):
    assert np.array_equal(a.ht_sine()._gen(test_df),
                          (talib.HT_SINE(test_df["a"].values.astype(float))[0]),
                          True)


class TestHTLeadSine:

  def test_calc_ht_sine(self):
    assert np.array_equal(a.ht_leadsine()._gen(test_df),
                          (talib.HT_SINE(test_df["a"])[1]), True)


class TestHTTrendmode:

  def test_calc_ht_trendmode(self):
    assert (a.ht_trendmode()._gen(test_df) == (talib.HT_TRENDMODE(
        test_df["a"]))).all()


class TestSecond:

  def test_calc_second(self):
    df = pd.DataFrame(
        {"a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 0, 0, 1),
        ]})

    assert (a.second()._gen(df) == pd.Series([0, 1])).all()
    assert a.second()._gen(df).dtype == np.int64


class TestMinute:

  def test_calc_minute(self):
    df = pd.DataFrame(
        {"a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 0, 1, 1),
        ]})

    assert (a.minute()._gen(df) == (pd.Series([0, 1]))).all()
    assert a.minute()._gen(df).dtype == int


class TestMinuteN:

  def test_calc_minute_n(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 0, 1, 1),
            datetime(2018, 1, 1, 0, 2, 2),
        ]
    })

    assert np.array_equal(
        a.minute_n(2)._gen(df), pd.Series([True, False, True]))


class TestMinuteNs:

  def test_calc_minute_ns(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 0, 1, 1),
            datetime(2018, 1, 1, 0, 2, 2),
            datetime(2018, 1, 1, 0, 3, 3),
        ]
    })

    result = a.minute_ns([2, 3]).set_features(df)

    assert result["minute_2_of_a"].equals(pd.Series([True, False, True, False]))
    assert result["minute_3_of_a"].equals(pd.Series([True, False, False, True]))


class TestHour:

  def test_calc_hour(self):
    df = pd.DataFrame(
        {"a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 1, 0, 1),
        ]})

    assert (a.hour().generate(df) == (np.array([0, 1]))).all()
    assert a.hour().generate(df).dtype == "int"


class TestHourN:

  def test_calc_hour_n(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 1, 1, 1),
            datetime(2018, 1, 1, 2, 2, 2),
        ]
    })

    assert np.array_equal(a.hour_n(2)._gen(df), pd.Series([True, False, True]))


class TestHourNs:

  def test_calc_hour_ns(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 1, 1, 1),
            datetime(2018, 1, 1, 2, 2, 2),
            datetime(2018, 1, 1, 3, 3, 3),
        ]
    })

    result = a.hour_ns([2, 3]).set_features(df, show_progress=True)

    assert result["hour_2_of_a"].equals(pd.Series([True, False, True, False]))
    assert result["hour_3_of_a"].equals(pd.Series([True, False, False, True]))


class TestDayOfWeek:

  def test_calc_day_of_week(self):
    df = pd.DataFrame(
        {"a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 2, 0, 0, 1),
        ]})

    assert (a.day_of_week()._gen(df) == (np.array([0, 1]))).all()
    assert a.day_of_week()._gen(df).dtype == "int"


class TestWeekOfYear:

  def test_calc_week_of_year(self):
    df = pd.DataFrame(
        {"a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 2, 0, 0, 1),
        ]})

    assert (a.week_of_year()._gen(df) == (np.array([1, 1]))).all()
    assert a.week_of_year()._gen(df).dtype == "int"


class TestDayOfMonth:

  def test_calc_day_of_month(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 5, 2, 0, 0, 1),
            datetime(2018, 8, 3, 0, 0, 1),
        ]
    })

    assert (a.day_of_month().generate(df) == np.array([1, 2, 3])).all()
    assert a.day_of_month().generate(df).dtype == "int"


class TestMonth:

  def test_calc_month(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 5, 2, 0, 0, 1),
            datetime(2018, 8, 3, 0, 0, 1),
        ]
    })

    assert (a.month().generate(df) == np.array([1, 5, 8])).all()
    assert a.month().generate(df).dtype == "int"


class TestToDatetime:

  def test_to_datetime(self):
    df = pd.DataFrame({"a": [1665194183, 1665194184]})
    df2 = pd.DataFrame({"a": [1665194183000, 1665194184000]})

    assert np.array_equal(
        a.to_datetime("s")._gen(df),
        pd.Series([
            datetime(2022, 10, 8, 1, 56, 23),
            datetime(2022, 10, 8, 1, 56, 24),
        ]))
    assert np.array_equal(
        a.to_datetime("ms")._gen(df2),
        pd.Series([
            datetime(2022, 10, 8, 1, 56, 23),
            datetime(2022, 10, 8, 1, 56, 24),
        ]))


class TestChain:

  def test_calc_chain(self):
    tdf = pd.DataFrame({"a": [1665194183000, 1665194184000]})
    dt = a.to_datetime("ms")
    fs = Features.many(a, dt, dt.minute())

    tdf = fs.set_features(tdf, show_progress=True)

    assert np.array_equal(tdf["minute_of_to_datetime_of_a"].values, [56, 56])
