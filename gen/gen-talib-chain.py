from glob import glob
from textwrap import indent

from gen.services.talib_feature import TalibFeature


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
from pl.feature_gen.feature_gen import FeatureGen

class TalibChain:
  def __init__(self, feature: FeatureGen):
    super().__init__()
    self.feature = feature
    
{indent(accessors, "  ")}
    """

  def _accessor_method(self, talib_feature: TalibFeature) -> str:
    args = ', '.join([
        f"{a.arg_def_component}" for a in talib_feature.init_args
        if a.name != "column"
    ])
    pass_args = (", " + ', '.join(
        [f"{a.name}" for a in talib_feature.init_args if a.name != "column"])
                ) if len(talib_feature.init_args) > 1 else ""

    return f"""\
def {talib_feature.name.lower()}(self, {args}) -> "FeatureGen":
  from pl.feature_gen.{talib_feature.kind}.talib.{talib_feature.file_name} import {talib_feature.name}Feature
  return {talib_feature.name}Feature(self.feature{pass_args})
"""

  def write(self):
    with open("pl/feature_gen/talib_chain.py", "w") as f:
      f.write(self.file_content)


def main():
  unary_features = [
      t for p in glob("pl/feature_gen/unary/talib/*.py")
      for t in TalibFeature.read("unary", p)
  ]
  chain_file = TalibChainFile(unary_features)
  chain_file.write()


if __name__ == "__main__":
  main()
