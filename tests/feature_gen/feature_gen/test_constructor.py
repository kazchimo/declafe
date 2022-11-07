import numpy as np
import pandas as pd
import talib

from declafe import col, c, FeatureGen
from declafe.feature_gen.binary import SARFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001)),
    "c": list(range(2001, 3001)),
    "d": list(range(3001, 4001)),
    "v": list(range(4001, 5001)),
})

a = col("a")
b = col("b")
_c = col("c")
d = col("d")
v = col("v")
_1 = c(1)


class TestCond:

  def test_cond(self):
    df = pd.DataFrame({
        "cond": [True, False],
        "a": [1, 2],
        "b": [3, 4],
    })
    f = FeatureGen.cond(col("cond"), col("a"), col("b"))

    assert f.generate(df).equals(pd.Series([1, 4]))


class TestAdx:

  def test_construct_adx(self):
    df = test_df.copy()
    result = FeatureGen.adx("a", "b", "d", 3)._gen(df)

    assert np.array_equal(result, talib.ADX(df["a"], df["b"], df["d"], 3), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.adx(a, b, d, 3)._gen(df)

    assert np.array_equal(result, talib.ADX(df["a"], df["b"], df["d"], 3), True)


class TestAdxes:

  def test_construct_adxes(self):
    df = test_df.copy()
    result = FeatureGen.adxes("a", "b", "d", [3, 5]).set_features(df)

    assert result["ADX_3_of_a_b_d"].equals(
        talib.ADX(df["a"], df["b"], df["d"], 3))
    assert result["ADX_5_of_a_b_d"].equals(
        talib.ADX(df["a"], df["b"], df["d"], 5))

  def test_accept_column(self):
    df = test_df.copy()
    result = FeatureGen.adxes(a, b, d, [3, 5]).set_features(df)

    assert result["ADX_3_of_a_b_d"].equals(
        talib.ADX(df["a"], df["b"], df["d"], 3))
    assert result["ADX_5_of_a_b_d"].equals(
        talib.ADX(df["a"], df["b"], df["d"], 5))


class TestSar:

  def test_return_sar(self):
    assert np.array_equal(
        FeatureGen.sar("a", "b")._gen(test_df),
        SARFeature("a", "b")._gen(test_df), True)

  def test_accept_col(self):
    assert np.array_equal(
        FeatureGen.sar(a, b)._gen(test_df),
        SARFeature("a", "b")._gen(test_df), True)


class TestSarext:

  def test_return_sarext(self):
    assert np.array_equal(
        FeatureGen.sarext("a", "b")._gen(test_df),
        talib.SAREXT(test_df["a"], test_df["b"]), True)

  def test_accept_col(self):
    assert np.array_equal(
        FeatureGen.sarext(a, b)._gen(test_df),
        talib.SAREXT(test_df["a"], test_df["b"]), True)


class TestMidprice:

  def test_return_midprice(self):
    assert np.array_equal(
        FeatureGen.midprice("a", "b", 3)._gen(test_df),
        talib.MIDPRICE(test_df["a"], test_df["b"], 3), True)

  def test_accept_col(self):
    assert np.array_equal(
        FeatureGen.midprice(a, b, 3)._gen(test_df),
        talib.MIDPRICE(test_df["a"], test_df["b"], 3), True)


class TestMidprices:

  def test_return_midprices(self):
    result = FeatureGen.midprices("a", "b", [3, 5]).set_features(test_df)

    assert result["MIDPRICE_3_a_b"].equals(
        talib.MIDPRICE(test_df["a"], test_df["b"], 3))
    assert result["MIDPRICE_5_a_b"].equals(
        talib.MIDPRICE(test_df["a"], test_df["b"], 5))

  def test_accept_col(self):
    result = FeatureGen.midprices(a, b, [3, 5]).set_features(test_df)

    assert result["MIDPRICE_3_a_b"].equals(
        talib.MIDPRICE(test_df["a"], test_df["b"], 3))
    assert result["MIDPRICE_5_a_b"].equals(
        talib.MIDPRICE(test_df["a"], test_df["b"], 5))


class TestAdxrs:

  def test_return_adxrs(self):
    df = test_df.copy()
    result = FeatureGen.adxrs("a", "b", "d", [3, 5]).set_features(df)

    assert result["ADXR_3_of_a_b_d"].equals(
        talib.ADXR(df["a"], df["b"], df["d"], 3))
    assert result["ADXR_5_of_a_b_d"].equals(
        talib.ADXR(df["a"], df["b"], df["d"], 5))


class TestAdxr:

  def test_return_adxr(self):
    df = test_df.copy()
    result = FeatureGen.adxr("a", "b", "d", 3)._gen(df)

    assert np.array_equal(result, talib.ADXR(df["a"], df["b"], df["d"], 3),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.adxr(a, b, d, 3)._gen(df)

    assert np.array_equal(result, talib.ADXR(df["a"], df["b"], df["d"], 3),
                          True)


class TestCcis:

  def test_return_ccis(self):
    df = test_df.copy()
    result = FeatureGen.ccis("a", "b", "d", [3, 5]).set_features(df)

    assert result["CCI_3_of_a_b_d"].equals(
        talib.CCI(df["a"], df["b"], df["d"], 3))
    assert result["CCI_5_of_a_b_d"].equals(
        talib.CCI(df["a"], df["b"], df["d"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.ccis(a, b, d, [3, 5]).set_features(df)

    assert result["CCI_3_of_a_b_d"].equals(
        talib.CCI(df["a"], df["b"], df["d"], 3))
    assert result["CCI_5_of_a_b_d"].equals(
        talib.CCI(df["a"], df["b"], df["d"], 5))


class TestCci:

  def test_return_cci(self):
    df = test_df.copy()
    result = FeatureGen.cci("a", "b", "d", 3)._gen(df)

    assert np.array_equal(result, talib.CCI(df["a"], df["b"], df["d"], 3), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cci(a, b, d, 3)._gen(df)

    assert np.array_equal(result, talib.CCI(df["a"], df["b"], df["d"], 3), True)


class TestAroonUp:

  def test_return_aroon_up(self):
    df = test_df.copy()
    result = FeatureGen.aroon_up("a", "b", 3)._gen(df)

    assert np.array_equal(result, talib.AROON(df["a"], df["b"], 3)[1], True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.aroon_up(a, b, 3)._gen(df)

    assert np.array_equal(result, talib.AROON(df["a"], df["b"], 3)[1], True)


class TestAroonUps:

  def test_return_aroon_ups(self):
    df = test_df.copy()
    result = FeatureGen.aroon_ups("a", "b", [3, 5]).set_features(df)

    assert result["AROONUp_3_a_b"].equals(talib.AROON(df["a"], df["b"], 3)[1])
    assert result["AROONUp_5_a_b"].equals(talib.AROON(df["a"], df["b"], 5)[1])

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.aroon_ups(a, b, [3, 5]).set_features(df)

    assert result["AROONUp_3_a_b"].equals(talib.AROON(df["a"], df["b"], 3)[1])
    assert result["AROONUp_5_a_b"].equals(talib.AROON(df["a"], df["b"], 5)[1])


class TestAroonDown:

  def test_return_aroon_down(self):
    df = test_df.copy()
    result = FeatureGen.aroon_down("a", "b", 3)._gen(df)

    assert np.array_equal(result, talib.AROON(df["a"], df["b"], 3)[0], True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.aroon_down(a, b, 3)._gen(df)

    assert np.array_equal(result, talib.AROON(df["a"], df["b"], 3)[0], True)


class TestAroonDowns:

  def test_return_aroon_downs(self):
    df = test_df.copy()
    result = FeatureGen.aroon_downs("a", "b", [3, 5]).set_features(df)

    assert result["AROONDown_3_a_b"].equals(talib.AROON(df["a"], df["b"], 3)[0])
    assert result["AROONDown_5_a_b"].equals(talib.AROON(df["a"], df["b"], 5)[0])

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.aroon_downs(a, b, [3, 5]).set_features(df)

    assert result["AROONDown_3_a_b"].equals(talib.AROON(df["a"], df["b"], 3)[0])
    assert result["AROONDown_5_a_b"].equals(talib.AROON(df["a"], df["b"], 5)[0])


class TestArronOsc:

  def test_return_arron_osc(self):
    df = test_df.copy()
    result = FeatureGen.aroon_osc("a", "b", 3)._gen(df)

    assert np.array_equal(result, talib.AROONOSC(df["a"], df["b"], 3), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.aroon_osc(a, b, 3)._gen(df)

    assert np.array_equal(result, talib.AROONOSC(df["a"], df["b"], 3), True)


class TestArronOscs:

  def test_return_arron_oscs(self):
    df = test_df.copy()
    result = FeatureGen.aroon_oscs("a", "b", [3, 5]).set_features(df)

    assert result["AROONOSC_3_a_b"].equals(talib.AROONOSC(df["a"], df["b"], 3))
    assert result["AROONOSC_5_a_b"].equals(talib.AROONOSC(df["a"], df["b"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.aroon_oscs(a, b, [3, 5]).set_features(df)

    assert result["AROONOSC_3_a_b"].equals(talib.AROONOSC(df["a"], df["b"], 3))
    assert result["AROONOSC_5_a_b"].equals(talib.AROONOSC(df["a"], df["b"], 5))


class TestBop:

  def test_return_bop(self):
    df = test_df.copy()
    result = FeatureGen.bop("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result, talib.BOP(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.bop(a, b, _c, d)._gen(df)

    assert np.array_equal(result, talib.BOP(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestDX:

  def test_return_dx(self):
    df = test_df.copy()
    result = FeatureGen.dx("a", "b", "c", 3)._gen(df)

    assert np.array_equal(result, talib.DX(df["a"], df["b"], df["c"], 3), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.dx(a, b, _c, 3)._gen(df)

    assert np.array_equal(result, talib.DX(df["a"], df["b"], df["c"], 3), True)


class TestDXES:

  def test_return_dxes(self):
    df = test_df.copy()
    result = FeatureGen.dxes("a", "b", "c", [3, 5]).set_features(df)

    assert result["DX_3_of_a_b_c"].equals(talib.DX(df["a"], df["b"], df["c"],
                                                   3))
    assert result["DX_5_of_a_b_c"].equals(talib.DX(df["a"], df["b"], df["c"],
                                                   5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.dxes(a, b, _c, [3, 5]).set_features(df)

    assert result["DX_3_of_a_b_c"].equals(talib.DX(df["a"], df["b"], df["c"],
                                                   3))
    assert result["DX_5_of_a_b_c"].equals(talib.DX(df["a"], df["b"], df["c"],
                                                   5))


class TestMFI:

  def test_return_mfi(self):
    df = test_df.copy()
    result = FeatureGen.mfi("a", "b", "c", "v", 3)._gen(df)

    assert np.array_equal(result,
                          talib.MFI(df["a"], df["b"], df["c"], df["v"], 3),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.mfi(a, b, _c, v, 3)._gen(df)

    assert np.array_equal(result,
                          talib.MFI(df["a"], df["b"], df["c"], df["v"], 3),
                          True)


class TestMFIS:

  def test_return_mfis(self):
    df = test_df.copy()
    result = FeatureGen.mfis("a", "b", "c", "v", [3, 5]).set_features(df)

    assert result["MFI_3_of_a_b_c_v"].equals(
        talib.MFI(df["a"], df["b"], df["c"], df["v"], 3))
    assert result["MFI_5_of_a_b_c_v"].equals(
        talib.MFI(df["a"], df["b"], df["c"], df["v"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.mfis(a, b, _c, v, [3, 5]).set_features(df)

    assert result["MFI_3_of_a_b_c_v"].equals(
        talib.MFI(df["a"], df["b"], df["c"], df["v"], 3))
    assert result["MFI_5_of_a_b_c_v"].equals(
        talib.MFI(df["a"], df["b"], df["c"], df["v"], 5))


class TestMinusDI:

  def test_return_minus_di(self):
    df = test_df.copy()
    result = FeatureGen.minus_di("a", "b", "c", 3)._gen(df)

    assert np.array_equal(result, talib.MINUS_DI(df["a"], df["b"], df["c"], 3),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.minus_di(a, b, _c, 3)._gen(df)

    assert np.array_equal(result, talib.MINUS_DI(df["a"], df["b"], df["c"], 3),
                          True)


class TestMinusDis:

  def test_return_minus_dis(self):
    df = test_df.copy()
    result = FeatureGen.minus_dis("a", "b", "c", [3, 5]).set_features(df)

    assert result["MINUS_DI_3_of_a_b_c"].equals(
        talib.MINUS_DI(df["a"], df["b"], df["c"], 3))
    assert result["MINUS_DI_5_of_a_b_c"].equals(
        talib.MINUS_DI(df["a"], df["b"], df["c"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.minus_dis(a, b, _c, [3, 5]).set_features(df)

    assert result["MINUS_DI_3_of_a_b_c"].equals(
        talib.MINUS_DI(df["a"], df["b"], df["c"], 3))
    assert result["MINUS_DI_5_of_a_b_c"].equals(
        talib.MINUS_DI(df["a"], df["b"], df["c"], 5))


class TestMinusDM:

  def test_return_minus_dm(self):
    df = test_df.copy()
    result = FeatureGen.minus_dm("a", "b", 3)._gen(df)

    assert np.array_equal(result, talib.MINUS_DM(df["a"], df["b"], 3), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.minus_dm(a, b, 3)._gen(df)

    assert np.array_equal(result, talib.MINUS_DM(df["a"], df["b"], 3), True)


class TestMinusDMs:

  def test_return_minus_dms(self):
    df = test_df.copy()
    result = FeatureGen.minus_dms("a", "b", [3, 5]).set_features(df)

    assert result["MINUS_DM_a_b_3"].equals(talib.MINUS_DM(df["a"], df["b"], 3))
    assert result["MINUS_DM_a_b_5"].equals(talib.MINUS_DM(df["a"], df["b"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.minus_dms(a, b, [3, 5]).set_features(df)

    assert result["MINUS_DM_a_b_3"].equals(talib.MINUS_DM(df["a"], df["b"], 3))
    assert result["MINUS_DM_a_b_5"].equals(talib.MINUS_DM(df["a"], df["b"], 5))


class TestPlusDI:

  def test_return_plus_di(self):
    df = test_df.copy()
    result = FeatureGen.plus_di("a", "b", "c", 3)._gen(df)

    assert np.array_equal(result, talib.PLUS_DI(df["a"], df["b"], df["c"], 3),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.plus_di(a, b, _c, 3)._gen(df)

    assert np.array_equal(result, talib.PLUS_DI(df["a"], df["b"], df["c"], 3),
                          True)


class TestPlusDIs:

  def test_return_plus_dis(self):
    df = test_df.copy()
    result = FeatureGen.plus_dis("a", "b", "c", [3, 5]).set_features(df)

    assert result["PLUS_DI_3_of_a_b_c"].equals(
        talib.PLUS_DI(df["a"], df["b"], df["c"], 3))
    assert result["PLUS_DI_5_of_a_b_c"].equals(
        talib.PLUS_DI(df["a"], df["b"], df["c"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.plus_dis(a, b, _c, [3, 5]).set_features(df)

    assert result["PLUS_DI_3_of_a_b_c"].equals(
        talib.PLUS_DI(df["a"], df["b"], df["c"], 3))
    assert result["PLUS_DI_5_of_a_b_c"].equals(
        talib.PLUS_DI(df["a"], df["b"], df["c"], 5))


class TestPlusDM:

  def test_return_plus_dm(self):
    df = test_df.copy()
    result = FeatureGen.plus_dm("a", "b", 3)._gen(df)

    assert np.array_equal(result, talib.PLUS_DM(df["a"], df["b"], 3), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.plus_dm(a, b, 3)._gen(df)

    assert np.array_equal(result, talib.PLUS_DM(df["a"], df["b"], 3), True)


class TestPlusDMS:

  def test_return_plus_dms(self):
    df = test_df.copy()
    result = FeatureGen.plus_dms("a", "b", [3, 5]).set_features(df)

    assert result["PLUS_DM_a_b_3"].equals(talib.PLUS_DM(df["a"], df["b"], 3))
    assert result["PLUS_DM_a_b_5"].equals(talib.PLUS_DM(df["a"], df["b"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.plus_dms(a, b, [3, 5]).set_features(df)

    assert result["PLUS_DM_a_b_3"].equals(talib.PLUS_DM(df["a"], df["b"], 3))
    assert result["PLUS_DM_a_b_5"].equals(talib.PLUS_DM(df["a"], df["b"], 5))


class TestSTOCHSlowd:

  def test_return_stoch(self):
    df = test_df.copy()
    result = FeatureGen.stoch_slowd("a", "b", "c", 5, 3, 10)._gen(df)

    assert np.array_equal(
        result,
        talib.STOCH(df["a"], df["b"], df["c"], 5, 3, slowd_period=10)[1], True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.stoch_slowd(a, b, _c, 5, 3, 10)._gen(df)

    assert np.array_equal(
        result,
        talib.STOCH(df["a"], df["b"], df["c"], 5, 3, slowd_period=10)[1], True)


class TestSTOCHSlowk:

  def test_return_stoch(self):
    df = test_df.copy()
    result = FeatureGen.stoch_slowk("a", "b", "c", 5, 3, 10)._gen(df)

    assert np.array_equal(
        result,
        talib.STOCH(df["a"], df["b"], df["c"], 5, 3, slowd_period=10)[0], True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.stoch_slowk(a, b, _c, 5, 3, 10)._gen(df)

    assert np.array_equal(
        result,
        talib.STOCH(df["a"], df["b"], df["c"], 5, 3, slowd_period=10)[0], True)


class TestSTOCHFFastk:

  def test_return_stoch(self):
    df = test_df.copy()
    result = FeatureGen.stochf_fastk("a", "b", "c", 5, 3)._gen(df)

    assert np.array_equal(result,
                          talib.STOCHF(df["a"], df["b"], df["c"], 5, 3)[0],
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.stochf_fastk(a, b, _c, 5, 3)._gen(df)

    assert np.array_equal(result,
                          talib.STOCHF(df["a"], df["b"], df["c"], 5, 3)[0],
                          True)


class TestSTOCHFFastd:

  def test_return_stoch(self):
    df = test_df.copy()
    result = FeatureGen.stochf_fastd("a", "b", "c", 5, 3)._gen(df)

    assert np.array_equal(result,
                          talib.STOCHF(df["a"], df["b"], df["c"], 5, 3)[1],
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.stochf_fastd(a, b, _c, 5, 3)._gen(df)

    assert np.array_equal(result,
                          talib.STOCHF(df["a"], df["b"], df["c"], 5, 3)[1],
                          True)


class TestULTOSC:

  def test_return_ultosc(self):
    df = test_df.copy()
    result = FeatureGen.ultosc("a", "b", "c", 3, 5, 7)._gen(df)

    assert np.array_equal(result,
                          talib.ULTOSC(df["a"], df["b"], df["c"], 3, 5, 7),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.ultosc(a, b, _c, 3, 5, 7)._gen(df)

    assert np.array_equal(result,
                          talib.ULTOSC(df["a"], df["b"], df["c"], 3, 5, 7),
                          True)


class TestWillr:

  def test_return_willr(self):
    df = test_df.copy()
    result = FeatureGen.willr("a", "b", "c", 5)._gen(df)

    assert np.array_equal(result, talib.WILLR(df["a"], df["b"], df["c"], 5),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.willr(a, b, _c, 5)._gen(df)

    assert np.array_equal(result, talib.WILLR(df["a"], df["b"], df["c"], 5),
                          True)


class TestWillrs:

  def test_return_willrs(self):
    df = test_df.copy()
    result = FeatureGen.willrs("a", "b", "c", [3, 5]).set_features(df)

    assert result["WILLR_3_of_a_b_c"].equals(
        talib.WILLR(df["a"], df["b"], df["c"], 3))
    assert result["WILLR_5_of_a_b_c"].equals(
        talib.WILLR(df["a"], df["b"], df["c"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.willrs(a, b, _c, [3, 5]).set_features(df)

    assert result["WILLR_3_of_a_b_c"].equals(
        talib.WILLR(df["a"], df["b"], df["c"], 3))
    assert result["WILLR_5_of_a_b_c"].equals(
        talib.WILLR(df["a"], df["b"], df["c"], 5))


class TestAD:

  def test_return_ad(self):
    df = test_df.copy()
    result = FeatureGen.ad("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result, talib.AD(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.ad(a, b, _c, d)._gen(df)

    assert np.array_equal(result, talib.AD(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestADOSC:

  def test_return_adosc(self):
    df = test_df.copy()
    result = FeatureGen.adosc("a", "b", "c", "d", 3, 5)._gen(df)

    assert np.array_equal(result,
                          talib.ADOSC(df["a"], df["b"], df["c"], df["d"], 3, 5),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.adosc(a, b, _c, d, 3, 5)._gen(df)

    assert np.array_equal(result,
                          talib.ADOSC(df["a"], df["b"], df["c"], df["d"], 3, 5),
                          True)


class TestOBV:

  def test_return_obv(self):
    df = test_df.copy()
    result = FeatureGen.obv("a", "b")._gen(df)

    assert np.array_equal(result, talib.OBV(df["a"], df["b"]))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.obv(a, b)._gen(df)

    assert np.array_equal(result, talib.OBV(df["a"], df["b"]))


class TestATR:

  def test_return_atr(self):
    df = test_df.copy()
    result = FeatureGen.atr("a", "b", "c", 5)._gen(df)

    assert np.array_equal(result, talib.ATR(df["a"], df["b"], df["c"], 5), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.atr(a, b, _c, 5)._gen(df)

    assert np.array_equal(result, talib.ATR(df["a"], df["b"], df["c"], 5), True)


class TestATRS:

  def test_return_atrs(self):
    df = test_df.copy()
    result = FeatureGen.atrs("a", "b", "c", [3, 5]).set_features(df)

    assert result["ATR_3_of_a_b_c"].equals(
        talib.ATR(df["a"], df["b"], df["c"], 3))
    assert result["ATR_5_of_a_b_c"].equals(
        talib.ATR(df["a"], df["b"], df["c"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.atrs(a, b, _c, [3, 5]).set_features(df)

    assert result["ATR_3_of_a_b_c"].equals(
        talib.ATR(df["a"], df["b"], df["c"], 3))
    assert result["ATR_5_of_a_b_c"].equals(
        talib.ATR(df["a"], df["b"], df["c"], 5))


class TestNATR:

  def test_return_natr(self):
    df = test_df.copy()
    result = FeatureGen.natr("a", "b", "c", 5)._gen(df)

    assert np.array_equal(result, talib.NATR(df["a"], df["b"], df["c"], 5),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.natr(a, b, _c, 5)._gen(df)

    assert np.array_equal(result, talib.NATR(df["a"], df["b"], df["c"], 5),
                          True)


class TestNATRS:

  def test_return_natrs(self):
    df = test_df.copy()
    result = FeatureGen.natrs("a", "b", "c", [3, 5]).set_features(df)

    assert result["NATR_3_of_a_b_c"].equals(
        talib.NATR(df["a"], df["b"], df["c"], 3))
    assert result["NATR_5_of_a_b_c"].equals(
        talib.NATR(df["a"], df["b"], df["c"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.natrs(a, b, _c, [3, 5]).set_features(df)

    assert result["NATR_3_of_a_b_c"].equals(
        talib.NATR(df["a"], df["b"], df["c"], 3))
    assert result["NATR_5_of_a_b_c"].equals(
        talib.NATR(df["a"], df["b"], df["c"], 5))


class TestTRANGE:

  def test_return_trange(self):
    df = test_df.copy()
    result = FeatureGen.trange("a", "b", "c")._gen(df)

    assert np.array_equal(result, talib.TRANGE(df["a"], df["b"], df["c"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.trange(a, b, _c)._gen(df)

    assert np.array_equal(result, talib.TRANGE(df["a"], df["b"], df["c"]), True)


class TestCDL2CROWS:

  def test_return_cdl2crows(self):
    df = test_df.copy()
    result = FeatureGen.cdl2crows("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDL2CROWS(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdl2crows(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDL2CROWS(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDL3BLACKCROWS:

  def test_return_cdl3blackcrows(self):
    df = test_df.copy()
    result = FeatureGen.cdl3blackcrows("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDL3BLACKCROWS(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdl3blackcrows(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDL3BLACKCROWS(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDL3INSIDE:

  def test_return_cdl3inside(self):
    df = test_df.copy()
    result = FeatureGen.cdl3inside("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDL3INSIDE(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdl3inside(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDL3INSIDE(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDL3LINESTRIKE:

  def test_return_cdl3linestrike(self):
    df = test_df.copy()
    result = FeatureGen.cdl3linestrike("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDL3LINESTRIKE(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdl3linestrike(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDL3LINESTRIKE(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDL3OUTSIDE:

  def test_return_cdl3outside(self):
    df = test_df.copy()
    result = FeatureGen.cdl3outside("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDL3OUTSIDE(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdl3outside(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDL3OUTSIDE(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDL3STARSINSOUTH:

  def test_return_cdl3starsinsouth(self):
    df = test_df.copy()
    result = FeatureGen.cdl3starsinsouth("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDL3STARSINSOUTH(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdl3starsinsouth(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDL3STARSINSOUTH(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDL3WHITESOLDIERS:

  def test_return_cdl3whitesoldiers(self):
    df = test_df.copy()
    result = FeatureGen.cdl3whitesoldiers("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDL3WHITESOLDIERS(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdl3whitesoldiers(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDL3WHITESOLDIERS(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLABANDONEDBABY:

  def test_return_cdlabandonedbaby(self):
    df = test_df.copy()
    result = FeatureGen.cdlabandonedbaby("a", "b", "c", "d", 0)._gen(df)

    assert np.array_equal(
        result, talib.CDLABANDONEDBABY(df["a"], df["b"], df["c"], df["d"], 0),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlabandonedbaby(a, b, _c, d, 0)._gen(df)

    assert np.array_equal(
        result, talib.CDLABANDONEDBABY(df["a"], df["b"], df["c"], df["d"], 0),
        True)


class TestCDLADVANCEBLOCK:

  def test_return_cdladvanceblock(self):
    df = test_df.copy()
    result = FeatureGen.cdladvanceblock("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLADVANCEBLOCK(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdladvanceblock(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLADVANCEBLOCK(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLBELTHOLD:

  def test_return_cdlbelthold(self):
    df = test_df.copy()
    result = FeatureGen.cdlbelthold("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLBELTHOLD(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlbelthold(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLBELTHOLD(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLBREAKAWAY:

  def test_return_cdlbreakaway(self):
    df = test_df.copy()
    result = FeatureGen.cdlbreakaway("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLBREAKAWAY(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlbreakaway(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLBREAKAWAY(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLCLOSINGMARUBOZU:

  def test_return_cdlclosingmarubozu(self):
    df = test_df.copy()
    result = FeatureGen.cdlclosingmarubozu("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLCLOSINGMARUBOZU(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlclosingmarubozu(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLCLOSINGMARUBOZU(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLCONCEALBABYSWALL:

  def test_return_cdlconcealbabyswall(self):
    df = test_df.copy()
    result = FeatureGen.cdlconcealbabyswall("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLCONCEALBABYSWALL(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlconcealbabyswall(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLCONCEALBABYSWALL(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLCOUNTERATTACK:

  def test_return_cdlcounterattack(self):
    df = test_df.copy()
    result = FeatureGen.cdlcounterattack("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLCOUNTERATTACK(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlcounterattack(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLCOUNTERATTACK(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLDARKCLOUDCOVER:

  def test_return_cdldarkcloudcover(self):
    df = test_df.copy()
    result = FeatureGen.cdldarkcloudcover("a", "b", "c", "d", 0)._gen(df)

    assert np.array_equal(
        result, talib.CDLDARKCLOUDCOVER(df["a"], df["b"], df["c"], df["d"], 0),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdldarkcloudcover(a, b, _c, d, 0)._gen(df)

    assert np.array_equal(
        result, talib.CDLDARKCLOUDCOVER(df["a"], df["b"], df["c"], df["d"], 0),
        True)


class TestCDLDOJI:

  def test_return_cdldoji(self):
    df = test_df.copy()
    result = FeatureGen.cdldoji("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLDOJI(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdldoji(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLDOJI(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLDOJISTAR:

  def test_return_cdldojistar(self):
    df = test_df.copy()
    result = FeatureGen.cdldojistar("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLDOJISTAR(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdldojistar(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLDOJISTAR(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLDRAGONFLYDOJI:

  def test_return_cdldragonflydoji(self):
    df = test_df.copy()
    result = FeatureGen.cdldragonflydoji("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLDRAGONFLYDOJI(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdldragonflydoji(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLDRAGONFLYDOJI(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLENGULFING:

  def test_return_cdlengulfing(self):
    df = test_df.copy()
    result = FeatureGen.cdlengulfing("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLENGULFING(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlengulfing(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLENGULFING(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLEVENINGDOJISTAR:

  def test_return_cdleveningdojistar(self):
    df = test_df.copy()
    result = FeatureGen.cdleveningdojistar("a", "b", "c", "d", 0)._gen(df)

    assert np.array_equal(
        result, talib.CDLEVENINGDOJISTAR(df["a"], df["b"], df["c"], df["d"], 0),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdleveningdojistar(a, b, _c, d, 0)._gen(df)

    assert np.array_equal(
        result, talib.CDLEVENINGDOJISTAR(df["a"], df["b"], df["c"], df["d"], 0),
        True)


class TestCDLEVENINGSTAR:

  def test_return_cdleveningstar(self):
    df = test_df.copy()
    result = FeatureGen.cdleveningstar("a", "b", "c", "d", 0)._gen(df)

    assert np.array_equal(
        result, talib.CDLEVENINGSTAR(df["a"], df["b"], df["c"], df["d"], 0),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdleveningstar(a, b, _c, d, 0)._gen(df)

    assert np.array_equal(
        result, talib.CDLEVENINGSTAR(df["a"], df["b"], df["c"], df["d"], 0),
        True)


class TestCDLGAPSIDESIDEWHITE:

  def test_return_cdlgapsidesidewhite(self):
    df = test_df.copy()
    result = FeatureGen.cdlgapsidesidewhite("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLGAPSIDESIDEWHITE(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlgapsidesidewhite(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLGAPSIDESIDEWHITE(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLGRAVESTONEDOJI:

  def test_return_cdlgravestonedoji(self):
    df = test_df.copy()
    result = FeatureGen.cdlgravestonedoji("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLGRAVESTONEDOJI(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlgravestonedoji(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLGRAVESTONEDOJI(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLHAMMER:

  def test_return_cdlhammer(self):
    df = test_df.copy()
    result = FeatureGen.cdlhammer("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLHAMMER(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlhammer(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLHAMMER(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLHANGINGMAN:

  def test_return_cdlhangingman(self):
    df = test_df.copy()
    result = FeatureGen.cdlhangingman("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLHANGINGMAN(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlhangingman(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLHANGINGMAN(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLHARAMI:

  def test_return_cdlharami(self):
    df = test_df.copy()
    result = FeatureGen.cdlharami("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLHARAMI(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlharami(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLHARAMI(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLHARAMICROSS:

  def test_return_cdlharamicross(self):
    df = test_df.copy()
    result = FeatureGen.cdlharamicross("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLHARAMICROSS(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlharamicross(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLHARAMICROSS(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLHIGHWAVE:

  def test_return_cdlhighwave(self):
    df = test_df.copy()
    result = FeatureGen.cdlhighwave("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLHIGHWAVE(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlhighwave(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLHIGHWAVE(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLHIKKAKE:

  def test_return_cdlhikkake(self):
    df = test_df.copy()
    result = FeatureGen.cdlhikkake("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLHIKKAKE(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlhikkake(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLHIKKAKE(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLHIKKAKEMOD:

  def test_return_cdlhikkakemod(self):
    df = test_df.copy()
    result = FeatureGen.cdlhikkakemod("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLHIKKAKEMOD(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlhikkakemod(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLHIKKAKEMOD(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLHOMINGPIGEON:

  def test_return_cdlhomingpigeon(self):
    df = test_df.copy()
    result = FeatureGen.cdlhomingpigeon("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLHOMINGPIGEON(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlhomingpigeon(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLHOMINGPIGEON(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLIDENTICAL3CROWS:

  def test_return_cdlidentical3crows(self):
    df = test_df.copy()
    result = FeatureGen.cdlidentical3crows("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLIDENTICAL3CROWS(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlidentical3crows(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLIDENTICAL3CROWS(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLINNECK:

  def test_return_cdlinneck(self):
    df = test_df.copy()
    result = FeatureGen.cdlinneck("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLINNECK(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlinneck(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLINNECK(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLINVERTEDHAMMER:

  def test_return_cdlinvertedhammer(self):
    df = test_df.copy()
    result = FeatureGen.cdlinvertedhammer("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLINVERTEDHAMMER(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlinvertedhammer(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLINVERTEDHAMMER(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLKICKING:

  def test_return_cdlkicking(self):
    df = test_df.copy()
    result = FeatureGen.cdlkicking("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLKICKING(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlkicking(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLKICKING(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLKICKINGBYLENGTH:

  def test_return_cdlkickingbylength(self):
    df = test_df.copy()
    result = FeatureGen.cdlkickingbylength("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLKICKINGBYLENGTH(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlkickingbylength(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLKICKINGBYLENGTH(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLLADDERBOTTOM:

  def test_return_cdlladderbottom(self):
    df = test_df.copy()
    result = FeatureGen.cdlladderbottom("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLLADDERBOTTOM(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlladderbottom(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLLADDERBOTTOM(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLLONGLEGGEDDOJI:

  def test_return_cdllongleggeddoji(self):
    df = test_df.copy()
    result = FeatureGen.cdllongleggeddoji("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLLONGLEGGEDDOJI(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdllongleggeddoji(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLLONGLEGGEDDOJI(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLLONGLINE:

  def test_return_cdllongline(self):
    df = test_df.copy()
    result = FeatureGen.cdllongline("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLLONGLINE(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdllongline(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLLONGLINE(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLMARUBOZU:

  def test_return_cdlmarubozu(self):
    df = test_df.copy()
    result = FeatureGen.cdlmarubozu("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLMARUBOZU(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlmarubozu(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLMARUBOZU(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLMATCHINGLOW:

  def test_return_cdlmatchinglow(self):
    df = test_df.copy()
    result = FeatureGen.cdlmatchinglow("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLMATCHINGLOW(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlmatchinglow(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLMATCHINGLOW(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLMATHOLD:

  def test_return_cdlmathold(self):
    df = test_df.copy()
    result = FeatureGen.cdlmathold("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLMATHOLD(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlmathold(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLMATHOLD(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLMORNINGDOJISTAR:

  def test_return_cdlmorningdojistar(self):
    df = test_df.copy()
    result = FeatureGen.cdlmorningdojistar("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLMORNINGDOJISTAR(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlmorningdojistar(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLMORNINGDOJISTAR(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLMORNINGSTAR:

  def test_return_cdlmorningstar(self):
    df = test_df.copy()
    result = FeatureGen.cdlmorningstar("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLMORNINGSTAR(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlmorningstar(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLMORNINGSTAR(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLONNECK:

  def test_return_cdlonneck(self):
    df = test_df.copy()
    result = FeatureGen.cdlonneck("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLONNECK(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlonneck(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLONNECK(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLPIERCING:

  def test_return_cdlpiercing(self):
    df = test_df.copy()
    result = FeatureGen.cdlpiercing("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLPIERCING(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlpiercing(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLPIERCING(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLRICKSHAWMAN:

  def test_return_cdlrickshawman(self):
    df = test_df.copy()
    result = FeatureGen.cdlrickshawman("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLRICKSHAWMAN(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlrickshawman(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLRICKSHAWMAN(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLRISEFALL3METHODS:

  def test_return_cdlrisefall3methods(self):
    df = test_df.copy()
    result = FeatureGen.cdlrisefall3methods("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLRISEFALL3METHODS(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlrisefall3methods(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLRISEFALL3METHODS(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLSEPARATINGLINES:

  def test_return_cdlseparatinglines(self):
    df = test_df.copy()
    result = FeatureGen.cdlseparatinglines("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLSEPARATINGLINES(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlseparatinglines(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLSEPARATINGLINES(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLSHOOTINGSTAR:

  def test_return_cdlshootingstar(self):
    df = test_df.copy()
    result = FeatureGen.cdlshootingstar("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLSHOOTINGSTAR(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlshootingstar(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLSHOOTINGSTAR(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLSHORTLINE:

  def test_return_cdlshortline(self):
    df = test_df.copy()
    result = FeatureGen.cdlshortline("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLSHORTLINE(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlshortline(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLSHORTLINE(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLSPINNINGTOP:

  def test_return_cdlspinningtop(self):
    df = test_df.copy()
    result = FeatureGen.cdlspinningtop("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLSPINNINGTOP(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlspinningtop(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLSPINNINGTOP(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLSTALLEDPATTERN:

  def test_return_cdlstalledpattern(self):
    df = test_df.copy()
    result = FeatureGen.cdlstalledpattern("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLSTALLEDPATTERN(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlstalledpattern(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLSTALLEDPATTERN(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLSTICKSANDWICH:

  def test_return_cdlsticksandwich(self):
    df = test_df.copy()
    result = FeatureGen.cdlsticksandwich("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLSTICKSANDWICH(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlsticksandwich(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLSTICKSANDWICH(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLTAKURI:

  def test_return_cdltakuri(self):
    df = test_df.copy()
    result = FeatureGen.cdltakuri("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLTAKURI(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdltakuri(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLTAKURI(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLTASUKIGAP:

  def test_return_cdltasukigap(self):
    df = test_df.copy()
    result = FeatureGen.cdltasukigap("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLTASUKIGAP(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdltasukigap(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLTASUKIGAP(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLTHRUSTING:

  def test_return_cdlthrusting(self):
    df = test_df.copy()
    result = FeatureGen.cdlthrusting("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLTHRUSTING(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlthrusting(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLTHRUSTING(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLTRISTAR:

  def test_return_cdltristar(self):
    df = test_df.copy()
    result = FeatureGen.cdltristar("a", "b", "c", "d")._gen(df)

    assert np.array_equal(result,
                          talib.CDLTRISTAR(df["a"], df["b"], df["c"], df["d"]),
                          True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdltristar(a, b, _c, d)._gen(df)

    assert np.array_equal(result,
                          talib.CDLTRISTAR(df["a"], df["b"], df["c"], df["d"]),
                          True)


class TestCDLUNIQUE3RIVER:

  def test_return_cdlunique3river(self):
    df = test_df.copy()
    result = FeatureGen.cdlunique3river("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLUNIQUE3RIVER(df["a"], df["b"], df["c"], df["d"]), True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlunique3river(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLUNIQUE3RIVER(df["a"], df["b"], df["c"], df["d"]), True)


class TestCDLUPSIDEGAP2CROWS:

  def test_return_cdlupsidegap2crows(self):
    df = test_df.copy()
    result = FeatureGen.cdlupsidegap2crows("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLUPSIDEGAP2CROWS(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlupsidegap2crows(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLUPSIDEGAP2CROWS(df["a"], df["b"], df["c"], df["d"]),
        True)


class TestCDLXSIDEGAP3METHODS:

  def test_return_cdlxsidegap3methods(self):
    df = test_df.copy()
    result = FeatureGen.cdlxsidegap3methods("a", "b", "c", "d")._gen(df)

    assert np.array_equal(
        result, talib.CDLXSIDEGAP3METHODS(df["a"], df["b"], df["c"], df["d"]),
        True)

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cdlxsidegap3methods(a, b, _c, d)._gen(df)

    assert np.array_equal(
        result, talib.CDLXSIDEGAP3METHODS(df["a"], df["b"], df["c"], df["d"]),
        True)
