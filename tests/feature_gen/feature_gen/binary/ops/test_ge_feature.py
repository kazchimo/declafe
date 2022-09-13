from declafe.feature_gen.binary import GEFeature


class TestOverrideFeatureName:
  def test_has_property(self):
    assert GEFeature("a", "b").override_feature_name is None
