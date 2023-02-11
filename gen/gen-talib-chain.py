from glob import glob
from textwrap import indent

from gen.services.talib_feature import TalibFeature

Aliases = {
    "ht_phasor_0": "ht_phasor_inphase",
    "ht_phasor_1": "ht_phasor_quadrature",
    "ht_sine_0": "ht_sine_sine",
    "ht_sine_1": "ht_sine_leadsine",
    "macdext_0": "macdext_macd",
    "macdext_1": "macdext_macdsignal",
    "macdext_2": "macdext_macdhist",
    "bbands_0": "bbands_upperband",
    "bbands_1": "bbands_middleband",
    "bbands_2": "bbands_lowerband",
    "macd_0": "macd_macd",
    "macd_1": "macd_macdsignal",
    "macd_2": "macd_macdhist",
    "macdfix_0": "macdfix_macd",
    "macdfix_1": "macdfix_macdsignal",
    "macdfix_2": "macdfix_macdhist",
    "mama_0": "mama_mama",
    "mama_1": "mama_fama",
    "stochrsi_0": "stochrsi_fastk",
    "stochrsi_1": "stochrsi_fastd",
}


class TalibChainFile:

  def __init__(self, talib_features: list[TalibFeature]):
    self.talib_features = talib_features

  @property
  def file_content(self) -> str:
    accessors = '\n'.join([
        self._accessor_method(talib_feature)
        for talib_feature in self.talib_features
    ])

    return f"""\
from declafe.pl.feature_gen.feature_gen import FeatureGen

class TalibChain:
  def __init__(self, feature: FeatureGen):
    super().__init__()
    self.feature = feature
    
{indent(accessors, "  ")}
    """

  def _accessor_method(self, talib_feature: TalibFeature) -> str:
    init_args = [
        f"{a.arg_def_component}" for a in talib_feature.init_args
        if a.type != "ColLike"
    ]
    args = (", " + ', '.join(init_args)) if len(init_args) > 0 else ""
    pass_args = ', '.join(
        [f"{a.name}" for a in talib_feature.init_args if a.type != "ColLike"])
    pass_args_component = (
        ", " + pass_args) if len(talib_feature.init_args) > 1 else ""
    method_name = talib_feature.name.lower()
    alias = Aliases.get(method_name)

    alias_def = f"""\
    
def {alias}(self{args}) -> "FeatureGen":
  return self.{method_name}({pass_args})"""

    return f"""\
def {method_name}(self{args}) -> "FeatureGen":
  from declafe.pl.feature_gen.{talib_feature.kind}.talib.{talib_feature.file_name} import {talib_feature.name}Feature
  return {talib_feature.name}Feature(self.feature{pass_args_component})
{alias_def if alias else ""}
"""

  def write(self):
    with open("declafe/pl/feature_gen/talib_chain.py", "w") as f:
      f.write(self.file_content)


def main():
  unary_features = [
      t for p in glob("declafe/pl/feature_gen/unary/talib/*.py")
      for t in TalibFeature.read(p)
  ]
  chain_file = TalibChainFile(unary_features)
  chain_file.write()


if __name__ == "__main__":
  main()
