from declafe.feature_gen.binary import LEFeature


class TestOverrideFeatureName:
  def test_has_property(self):
    assert LEFeature("a", "b").override_feature_name is None
