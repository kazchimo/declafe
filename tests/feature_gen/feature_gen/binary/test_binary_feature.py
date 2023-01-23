import numpy as np
import pandas as pd

from declafe import col, c
from declafe.feature_gen.binary import BinaryFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")


class AddFeature(BinaryFeature):

  def bigen(self, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left + right

  def _feature_name(self) -> str:
    return f"{self.left} + {self.right}"


class TestWithConst:

  def test_gen_using_const(self):
    df = test_df.copy()
    f = AddFeature(a, c(1)).to_features
    result = f.set_features(df)

    assert result["a + 1"].equals(df["a"] + 1)
