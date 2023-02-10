from glob import glob

from gen.services.talib_feature import TalibFeature
from textwrap import indent


class TalibConstructorFile:

  def __init__(self, talib_features: list[TalibFeature]):
    self.talib_features = talib_features

  @property
  def file_content(self) -> str:
    constructors = '\n'.join([
        self._constructor_method(talib_feature)
        for talib_feature in self.talib_features
    ])
    return f"""\
from declafe.pl.feature_gen.types import ColLike
from declafe.pl.feature_gen.feature_gen import FeatureGen

# noinspection PyMethodMayBeStatic,SpellCheckingInspection
class TalibConstructor:
  def __init__(self):
    super().__init__()

{indent(constructors, "  ")}
    """

  def _constructor_method(self, talib_feature: TalibFeature) -> str:
    args = ', '.join([
        f"{a.arg_def_component}" for a in talib_feature.init_args
        if a.name != "column"
    ])
    pass_args = (', '.join([
        f"{a.name}" for a in talib_feature.init_args if a.name != "column"
    ])) if len(talib_feature.init_args) > 1 else ""

    return f"""\
def {talib_feature.name.lower()}(self, {args}) -> "FeatureGen":
  from declafe.pl.feature_gen.{talib_feature.kind}.talib.{talib_feature.file_name} import {talib_feature.name}Feature
  return {talib_feature.name}Feature({pass_args})
"""

  def write(self):
    with open("pl/feature_gen/talib_constructor.py", "w") as f:
      f.write(self.file_content)


def main():
  features = [
      t for p in glob("pl/feature_gen/*/talib/*.py")
      for t in TalibFeature.read(p) if "unary" not in t.path
  ]

  chain_file = TalibConstructorFile(features)
  chain_file.write()


if __name__ == "__main__":
  main()
