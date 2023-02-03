from pl.feature_gen.feature_gen import FeatureGen
from pl.feature_gen.features import Features


def features(*fs: FeatureGen) -> Features:
  return Features(list(fs))
