import numpy as np
import pandas as pd

from declafe import col

test_df = pd.DataFrame({
    "b1": [True, False, True, False],
    "b2": [True, True, False, False],
})

b1 = col("b1")
b2 = col("b2")


class TestEq:

  def test_eq(self):
    assert np.array_equal((b1 == b2)._gen(test_df),
                          pd.Series([True, False, False, True]))

  def test_with_constant(self):
    assert np.array_equal((b1 == True)._gen(test_df),
                          pd.Series([True, False, True, False]))
    assert np.array_equal((b1 == False)._gen(test_df),
                          pd.Series([False, True, False, True]))

  def test_handle_float(self):
    assert np.array_equal((b1 == 1.0)._gen(test_df),
                          pd.Series([True, False, True, False]))
    assert np.array_equal((b1 == 0.0)._gen(test_df),
                          pd.Series([False, True, False, True]))

  def test_dtype(self):
    assert (b1 == b2)._gen(test_df).dtype == bool

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") == 1)._gen(df).dtype == bool


class TestNe:

  def test_ne(self):
    assert np.array_equal((b1 != b2)._gen(test_df),
                          pd.Series([False, True, True, False]))

  def test_with_constant(self):
    assert np.array_equal((b1 != True)._gen(test_df),
                          pd.Series([False, True, False, True]))
    assert np.array_equal((b1 != False)._gen(test_df),
                          pd.Series([True, False, True, False]))

  def test_handle_float(self):
    assert np.array_equal((b1 != 1.0)._gen(test_df),
                          pd.Series([False, True, False, True]))
    assert np.array_equal((b1 != 0.0)._gen(test_df),
                          pd.Series([True, False, True, False]))

  def test_dtype(self):
    assert (b1 != b2)._gen(test_df).dtype == bool

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") == 1)._gen(df).dtype == bool


class TestAdd:

  def test_add(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert np.array_equal((col("a") + col("b"))._gen(df), pd.Series([5, 7, 9]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((col("a") + 1)._gen(df), pd.Series([2, 3, 4]))

  def test_from_left(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((1 + col("a"))._gen(df), pd.Series([2, 3, 4]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") + 1)._gen(df).dtype == int

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") + 1)._gen(df).dtype == float

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") + 1)._gen(df).dtype == float


class TestSub:

  def test_sub(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert np.array_equal((col("a") - col("b"))._gen(df),
                          pd.Series([-3, -3, -3]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((col("a") - 1)._gen(df), pd.Series([0, 1, 2]))

  def test_from_left(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((1 - col("a"))._gen(df), pd.Series([0, -1, -2]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") - 1)._gen(df).dtype == int

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") - 1)._gen(df).dtype == float

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") - 1)._gen(df).dtype == float


class TestMul:

  def test_mul(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert np.array_equal((col("a") * col("b"))._gen(df), pd.Series([4, 10,
                                                                     18]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((col("a") * 2)._gen(df), pd.Series([2, 4, 6]))

  def test_from_left(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((2 * col("a"))._gen(df), pd.Series([2, 4, 6]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") * 1)._gen(df).dtype == int

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") * 1)._gen(df).dtype == float

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") * 1)._gen(df).dtype == float


class TestMod:

  def test_mod(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert np.array_equal((col("a") % col("b"))._gen(df), pd.Series([1, 2, 3]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((col("a") % 2)._gen(df), pd.Series([1, 0, 1]))

  def test_from_left(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((2 % col("a"))._gen(df), pd.Series([0, 0, 2]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") % 1)._gen(df).dtype == int

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") % 1)._gen(df).dtype == float

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") % 1)._gen(df).dtype == float


class TestTrueDiv:

  def test_true_div(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert np.array_equal((col("a") / col("b"))._gen(df),
                          pd.Series([0.25, 0.4, 0.5]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((col("a") / 2)._gen(df), pd.Series([0.5, 1, 1.5]))

  def test_from_left(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((2 / col("a"))._gen(df),
                          pd.Series([2, 1, 0.6666666666666666]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") / 1)._gen(df).dtype == float

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") / 1)._gen(df).dtype == float

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") / 1)._gen(df).dtype == float


class TestGt:

  def test_gt(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert np.array_equal((col("a") > col("b"))._gen(df),
                          pd.Series([False, False, False]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((col("a") > 2)._gen(df),
                          pd.Series([False, False, True]))

  def test_from_left(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((2 > col("a"))._gen(df),
                          pd.Series([True, False, False]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") > 1)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") > 1)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") > 1)._gen(df).dtype == bool


class TestLt:

  def test_lt(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert np.array_equal((col("a") < col("b"))._gen(df),
                          pd.Series([True, True, True]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((col("a") < 2)._gen(df),
                          pd.Series([True, False, False]))

  def test_from_left(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((2 < col("a"))._gen(df),
                          pd.Series([False, False, True]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") < 1)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") < 1)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") < 1)._gen(df).dtype == bool


class TestGe:

  def test_ge(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert np.array_equal((col("a") >= col("b"))._gen(df),
                          pd.Series([False, False, False]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((col("a") >= 2)._gen(df),
                          pd.Series([False, True, True]))

  def test_from_left(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((2 >= col("a"))._gen(df),
                          pd.Series([True, True, False]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") >= 1)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") >= 1)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") >= 1)._gen(df).dtype == bool


class TestLe:

  def test_le(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert np.array_equal((col("a") <= col("b"))._gen(df),
                          pd.Series([True, True, True]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((col("a") <= 2)._gen(df),
                          pd.Series([True, True, False]))

  def test_from_left(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert np.array_equal((2 <= col("a"))._gen(df),
                          pd.Series([False, True, True]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") <= 1)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") <= 1)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") <= 1)._gen(df).dtype == bool


class TestAnd:

  def test_and(self):
    assert np.array_equal((b1 & b2)._gen(test_df),
                          pd.Series([True, False, False, False]))

  def test_with_const(self):
    assert np.array_equal((b1 & True)._gen(test_df),
                          pd.Series([True, False, True, False]))
    assert np.array_equal((b1 & False)._gen(test_df),
                          pd.Series([False, False, False, False]))

  def test_from_left(self):
    assert np.array_equal((True & b1)._gen(test_df),
                          pd.Series([True, False, True, False]))
    assert np.array_equal((False & b1)._gen(test_df),
                          pd.Series([False, False, False, False]))

  def test_handle_float(self):
    assert np.array_equal((b1 & 1.0)._gen(test_df),
                          pd.Series([True, False, True, False]))
    assert np.array_equal((b1 & 0.0)._gen(test_df),
                          pd.Series([False, False, False, False]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") & True)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") & True)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") & True)._gen(df).dtype == bool


class TestOr:

  def test_or(self):
    assert np.array_equal((b1 | b2)._gen(test_df),
                          pd.Series([True, True, True, False]))

  def test_with_const(self):
    assert np.array_equal((b1 | True)._gen(test_df),
                          pd.Series([True, True, True, True]))
    assert np.array_equal((b1 | False)._gen(test_df),
                          pd.Series([True, False, True, False]))

  def test_from_left(self):
    assert np.array_equal((True | b1)._gen(test_df),
                          pd.Series([True, True, True, True]))
    assert np.array_equal((False | b1)._gen(test_df),
                          pd.Series([True, False, True, False]))

  def test_handle_float(self):
    assert np.array_equal((b1 | 1.0)._gen(test_df),
                          pd.Series([True, True, True, True]))
    assert np.array_equal((b1 | 0.0)._gen(test_df),
                          pd.Series([True, False, True, False]))

  def test_dtype(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") | True)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    assert (col("a") | True)._gen(df).dtype == bool

    df = pd.DataFrame({"a": [1, 2, 3]}).astype(object)
    assert (col("a") | True)._gen(df).dtype == bool
