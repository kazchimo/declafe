import re

from gen.services.talib_chain_def import TalibChainDef


class TalibChainTests:

  def __init__(self, chain_defs: list[TalibChainDef]):
    self.chain_defs = chain_defs

  @property
  def file_content(self) -> str:
    tests = '\n'.join(
        [self._test_content(chain_def) for chain_def in self.chain_defs])

    return f"""\
import talib
import polars as pl
import pl.feature_gen as fg

df = pl.DataFrame({{
      "close": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "open": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "high": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "low": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "volume": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }})

{tests}
"""

  def _test_content(self, chain_def: TalibChainDef) -> str:
    idx_component = f"[{chain_def.talib_method_idx}]" if chain_def.talib_method_idx is not None else ""
    arg_component = ", ".join(
        [arg.as_pass_component(arg.test_value) for arg in chain_def.args])
    fill_na_component = "" if chain_def.def_name == "ht_trendmode" else ".fill_nan(0)"

    return f"""\
class Test{chain_def.def_name.capitalize()}:
  def test_{chain_def.def_name}(self):
    gen = fg.col("close").talib.{chain_def.def_name}({arg_component})
    name = "{chain_def.def_name.upper()}({", ".join([a.test_value for a in chain_def.args])})(close)"
    assert gen(df){fill_na_component}.series_equal(
      talib.{chain_def.talib_method_name}(df["close"], {arg_component}){idx_component}.alias(name){fill_na_component}
    )
"""

  def write(self):
    with open("tests/pl/feature_gen/test_talib_chain.py", "w") as f:
      f.write(self.file_content)


def main():
  def_regex = re.compile(r'def\s+(\w+)\((.*?)\) -> "FeatureGen":',
                         re.MULTILINE | re.DOTALL)
  with open("pl/feature_gen/talib_chain.py", "r") as f:
    chain_defs = [
        TalibChainDef(l[0], l[1].replace(" ", "").replace("\n", ""))
        for l in def_regex.findall("\n".join(f.read().split("\n")[8:]))
    ]

  chain_test_file = TalibChainTests(chain_defs)
  chain_test_file.write()


if __name__ == "__main__":
  main()
