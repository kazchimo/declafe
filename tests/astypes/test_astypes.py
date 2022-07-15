import pandas as pd

from declafe.astype import AsTypes

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["a", "b", "c"]})


class TestSetTypes:

  def test_set_types(self):
    df1 = df.copy()
    astypes = AsTypes.from_type("int64", "uint8", df1)
    astypes.set_types(df1)

    assert df1.dtypes.equals(
        pd.Series({
            "a": "uint8",
            "b": "uint8",
            "c": "object"
        }))
