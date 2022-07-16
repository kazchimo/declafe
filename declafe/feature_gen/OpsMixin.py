from abc import abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from ..feature_gen import FeatureGen


class OpsMixin:

  @abstractmethod
  def _self(self) -> "FeatureGen":
    raise NotImplementedError

  @staticmethod
  def _bc():
    from ..binary.BiComposeFeature import BiComposeFeature
    return BiComposeFeature

  @staticmethod
  def _conv(a: Any):
    from ..ConstFeature import ConstFeature
    return ConstFeature.conv(a)

  def __eq__(self, other):
    from ..binary import EqualFeature, BiComposeFeature

    return BiComposeFeature.make(left=self._self(),
                                 right=self._conv(other),
                                 to=EqualFeature)

  def __ne__(self, other):
    return (self == other).flip_bool()

  def __add__(self, other):
    from ..binary import AddFeature
    return self._bc().make(left=self._self(), right=self._conv(other), to=AddFeature)

  def __sub__(self, other):
    from ..binary import SubFeature

    return self._bc().make(self._self(), self._conv(other), SubFeature)

  def __mul__(self, other):
    from ..binary import ProductFeature

    return self._bc().make(self._self(), self._conv(other), ProductFeature)

  def __mod__(self, other):
    from ..binary import ModFeature

    return self._bc().make(self._self(), self._conv(other), ModFeature)

  def __truediv__(self, other: "FeatureGen") -> "FeatureGen":
    from ..binary import DivideFeature

    return self._bc().make(self._self(), self._conv(other), DivideFeature)

  def __gt__(self, other):
    from ..binary import IsGreaterFeature

    return self._bc().make(self._self(), self._conv(other), IsGreaterFeature)

  def __lt__(self, other):
    from ..binary import IsLessFeature

    return self._bc().make(self._self(), self._conv(other), IsLessFeature)

  def __ge__(self, other):
    from ..binary import GEFeature

    return self._bc().make(self._self(), self._conv(other), GEFeature)

  def __le__(self, other):
    from ..binary import LEFeature

    return self._bc().make(self._self(), self._conv(other), LEFeature)
