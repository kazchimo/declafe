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


class TestAdx:

  def test_construct_adx(self):
    df = test_df.copy()
    result = FeatureGen.adx("a", "b", "d", 3).gen(df)

    assert result.equals(talib.ADX(df["a"], df["b"], df["d"], 3))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.adx(a, b, d, 3).gen(df)

    assert result.equals(talib.ADX(df["a"], df["b"], df["d"], 3))


class TestAdxes:

  def test_construct_adxes(self):
    df = test_df.copy()
    result = FeatureGen.adxes("a", "b", "d", [3, 5]).set_features(df)

    assert result["ADX_3_of_d"].equals(talib.ADX(df["a"], df["b"], df["d"], 3))
    assert result["ADX_5_of_d"].equals(talib.ADX(df["a"], df["b"], df["d"], 5))

  def test_accept_column(self):
    df = test_df.copy()
    result = FeatureGen.adxes(a, b, d, [3, 5]).set_features(df)

    assert result["ADX_3_of_d"].equals(talib.ADX(df["a"], df["b"], df["d"], 3))
    assert result["ADX_5_of_d"].equals(talib.ADX(df["a"], df["b"], df["d"], 5))


class TestSar:

  def test_return_sar(self):
    assert FeatureGen.sar("a", "b") \
      .gen(test_df) \
      .equals(SARFeature("a", "b").gen(test_df))

  def test_accept_col(self):
    assert FeatureGen.sar(a, b) \
      .gen(test_df) \
      .equals(SARFeature("a", "b").gen(test_df))


class TestSarext:

  def test_return_sarext(self):
    assert FeatureGen.sarext("a", "b") \
      .gen(test_df) \
      .equals(talib.SAREXT(test_df["a"], test_df["b"]))

  def test_accept_col(self):
    assert FeatureGen.sarext(a, b) \
      .gen(test_df) \
      .equals(talib.SAREXT(test_df["a"], test_df["b"]))


class TestMidprice:

  def test_return_midprice(self):
    assert FeatureGen.midprice("a", "b") \
      .gen(test_df) \
      .equals(talib.MIDPRICE(test_df["a"], test_df["b"]))

  def test_accept_col(self):
    assert FeatureGen.midprice(a, b) \
      .gen(test_df) \
      .equals(talib.MIDPRICE(test_df["a"], test_df["b"]))


class TestAdxrs:

  def test_return_adxrs(self):
    df = test_df.copy()
    result = FeatureGen.adxrs("a", "b", "d", [3, 5]).set_features(df)

    assert result["ADXR_3_of_d"].equals(talib.ADXR(df["a"], df["b"], df["d"],
                                                   3))
    assert result["ADXR_5_of_d"].equals(talib.ADXR(df["a"], df["b"], df["d"],
                                                   5))


class TestAdxr:

  def test_return_adxr(self):
    df = test_df.copy()
    result = FeatureGen.adxr("a", "b", "d", 3).gen(df)

    assert result.equals(talib.ADXR(df["a"], df["b"], df["d"], 3))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.adxr(a, b, d, 3).gen(df)

    assert result.equals(talib.ADXR(df["a"], df["b"], df["d"], 3))


class TestCcis:

  def test_return_ccis(self):
    df = test_df.copy()
    result = FeatureGen.ccis("a", "b", "d", [3, 5]).set_features(df)

    assert result["CCI_3_of_d"].equals(talib.CCI(df["a"], df["b"], df["d"], 3))
    assert result["CCI_5_of_d"].equals(talib.CCI(df["a"], df["b"], df["d"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.ccis(a, b, d, [3, 5]).set_features(df)

    assert result["CCI_3_of_d"].equals(talib.CCI(df["a"], df["b"], df["d"], 3))
    assert result["CCI_5_of_d"].equals(talib.CCI(df["a"], df["b"], df["d"], 5))


class TestCci:

  def test_return_cci(self):
    df = test_df.copy()
    result = FeatureGen.cci("a", "b", "d", 3).gen(df)

    assert result.equals(talib.CCI(df["a"], df["b"], df["d"], 3))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.cci(a, b, d, 3).gen(df)

    assert result.equals(talib.CCI(df["a"], df["b"], df["d"], 3))


class TestAroonUp:

  def test_return_aroon_up(self):
    df = test_df.copy()
    result = FeatureGen.aroon_up("a", "b", 3).gen(df)

    assert result.equals(talib.AROON(df["a"], df["b"], 3)[1])

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.aroon_up(a, b, 3).gen(df)

    assert result.equals(talib.AROON(df["a"], df["b"], 3)[1])


class TestAroonUps:

  def test_return_aroon_ups(self):
    df = test_df.copy()
    result = FeatureGen.aroon_ups("a", "b", [3, 5]).set_features(df)

    assert result["AROONUp_3"].equals(talib.AROON(df["a"], df["b"], 3)[1])
    assert result["AROONUp_5"].equals(talib.AROON(df["a"], df["b"], 5)[1])

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.aroon_ups(a, b, [3, 5]).set_features(df)

    assert result["AROONUp_3"].equals(talib.AROON(df["a"], df["b"], 3)[1])
    assert result["AROONUp_5"].equals(talib.AROON(df["a"], df["b"], 5)[1])


class TestAroonDown:

  def test_return_aroon_down(self):
    df = test_df.copy()
    result = FeatureGen.aroon_down("a", "b", 3).gen(df)

    assert result.equals(talib.AROON(df["a"], df["b"], 3)[0])

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.aroon_down(a, b, 3).gen(df)

    assert result.equals(talib.AROON(df["a"], df["b"], 3)[0])


class TestAroonDowns:

  def test_return_aroon_downs(self):
    df = test_df.copy()
    result = FeatureGen.aroon_downs("a", "b", [3, 5]).set_features(df)

    assert result["AROONDown_3"].equals(talib.AROON(df["a"], df["b"], 3)[0])
    assert result["AROONDown_5"].equals(talib.AROON(df["a"], df["b"], 5)[0])

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.aroon_downs(a, b, [3, 5]).set_features(df)

    assert result["AROONDown_3"].equals(talib.AROON(df["a"], df["b"], 3)[0])
    assert result["AROONDown_5"].equals(talib.AROON(df["a"], df["b"], 5)[0])


class TestArronOsc:

  def test_return_arron_osc(self):
    df = test_df.copy()
    result = FeatureGen.arron_osc("a", "b", 3).gen(df)

    assert result.equals(talib.AROONOSC(df["a"], df["b"], 3))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.arron_osc(a, b, 3).gen(df)

    assert result.equals(talib.AROONOSC(df["a"], df["b"], 3))


class TestArronOscs:

  def test_return_arron_oscs(self):
    df = test_df.copy()
    result = FeatureGen.arron_oscs("a", "b", [3, 5]).set_features(df)

    assert result["AROONOSC_3"].equals(talib.AROONOSC(df["a"], df["b"], 3))
    assert result["AROONOSC_5"].equals(talib.AROONOSC(df["a"], df["b"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.arron_oscs(a, b, [3, 5]).set_features(df)

    assert result["AROONOSC_3"].equals(talib.AROONOSC(df["a"], df["b"], 3))
    assert result["AROONOSC_5"].equals(talib.AROONOSC(df["a"], df["b"], 5))


class TestBop:

  def test_return_bop(self):
    df = test_df.copy()
    result = FeatureGen.bop("a", "b", "c", "d").gen(df)

    assert result.equals(talib.BOP(df["a"], df["b"], df["c"], df["d"]))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.bop(a, b, _c, d).gen(df)

    assert result.equals(talib.BOP(df["a"], df["b"], df["c"], df["d"]))


class TestDX:

  def test_return_dx(self):
    df = test_df.copy()
    result = FeatureGen.dx("a", "b", "c", 3).gen(df)

    assert result.equals(talib.DX(df["a"], df["b"], df["c"], 3))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.dx(a, b, _c, 3).gen(df)

    assert result.equals(talib.DX(df["a"], df["b"], df["c"], 3))


class TestDXES:

  def test_return_dxes(self):
    df = test_df.copy()
    result = FeatureGen.dxes("a", "b", "c", [3, 5]).set_features(df)

    assert result["DX_3_of_c"].equals(talib.DX(df["a"], df["b"], df["c"], 3))
    assert result["DX_5_of_c"].equals(talib.DX(df["a"], df["b"], df["c"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.dxes(a, b, _c, [3, 5]).set_features(df)

    assert result["DX_3_of_c"].equals(talib.DX(df["a"], df["b"], df["c"], 3))
    assert result["DX_5_of_c"].equals(talib.DX(df["a"], df["b"], df["c"], 5))


class TestMFI:

  def test_return_mfi(self):
    df = test_df.copy()
    result = FeatureGen.mfi("a", "b", "c", "v", 3).gen(df)

    assert result.equals(talib.MFI(df["a"], df["b"], df["c"], df["v"], 3))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.mfi(a, b, _c, v, 3).gen(df)

    assert result.equals(talib.MFI(df["a"], df["b"], df["c"], df["v"], 3))


class TestMFIS:

  def test_return_mfis(self):
    df = test_df.copy()
    result = FeatureGen.mfis("a", "b", "c", "v", [3, 5]).set_features(df)

    assert result["MFI_a_b_c_v_3"].equals(
        talib.MFI(df["a"], df["b"], df["c"], df["v"], 3))
    assert result["MFI_a_b_c_v_5"].equals(
        talib.MFI(df["a"], df["b"], df["c"], df["v"], 5))

  def test_accept_col(self):
    df = test_df.copy()
    result = FeatureGen.mfis(a, b, _c, v, [3, 5]).set_features(df)

    assert result["MFI_a_b_c_v_3"].equals(
        talib.MFI(df["a"], df["b"], df["c"], df["v"], 3))
    assert result["MFI_a_b_c_v_5"].equals(
        talib.MFI(df["a"], df["b"], df["c"], df["v"], 5))
