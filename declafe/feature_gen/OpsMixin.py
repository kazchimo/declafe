from abc import ABC


class OpxMixin(ABC):
  def __eq__(self, other):
    from lib.features.binary import EqualFeature, BiComposeFeature
    from lib.features import ConstFeature

    return BiComposeFeature.make(left=self, right=ConstFeature.make(other), to=EqualFeature)

  def __ne__(self, other):
    return (self == other).flip_bool()

  def __add__(self, other):
    from lib.features.binary import AddFeature
    from lib.features import BiComposeFeature
    return BiComposeFeature.make(left=self, right=other, to=AddFeature)

  def __sub__(self, other):
    from lib.features import BiComposeFeature
    from lib.features.binary import SubFeature
    from lib.features import ConstFeature

    return BiComposeFeature.make(self, ConstFeature.make(other), SubFeature)

  def __mul__(self, other):
    from lib.features import BiComposeFeature
    from lib.features.binary import ProductFeature
    from lib.features import ConstFeature

    return BiComposeFeature.make(self, ConstFeature.make(other), ProductFeature)

  def __mod__(self, other):
    from lib.features import BiComposeFeature
    from lib.features.binary import ModFeature
    from lib.features import ConstFeature

    return BiComposeFeature.make(self, ConstFeature.make(other), ModFeature)

  def __truediv__(self, other: "FeatureGen") -> "FeatureGen":
    from lib.features import BiComposeFeature
    from lib.features.binary import DivideFeature
    from lib.features import ConstFeature

    return BiComposeFeature.make(self, ConstFeature.make(other), DivideFeature)

  def __gt__(self, other):
    from lib.features import BiComposeFeature
    from lib.features.binary import IsGreaterFeature
    from lib.features import ConstFeature

    return BiComposeFeature.make(self, ConstFeature.make(other), IsGreaterFeature)

  def __lt__(self, other):
    from lib.features import BiComposeFeature
    from lib.features.binary import IsLessFeature
    from lib.features import ConstFeature

    return BiComposeFeature.make(self, ConstFeature.make(other), IsLessFeature)

  def __ge__(self, other):
    from lib.features import BiComposeFeature
    from lib.features.binary import GEFeature
    from lib.features import ConstFeature

    return BiComposeFeature.make(self, ConstFeature.make(other), GEFeature)

  def __le__(self, other):
    from lib.features import BiComposeFeature
    from lib.features.binary import LEFeature
    from lib.features import ConstFeature

    return BiComposeFeature.make(self, ConstFeature.make(other), LEFeature)
