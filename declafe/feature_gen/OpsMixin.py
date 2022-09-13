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
    from declafe.feature_gen.binary import BiComposeFeature
    return BiComposeFeature

  @staticmethod
  def _conv(a: Any):
    from declafe.feature_gen.ConstFeature import ConstFeature
    return ConstFeature.conv(a)

  def __eq__(self, other):
    from .binary import BiComposeFeature
    from .binary.ops import EqualFeature

    return BiComposeFeature.make(left=self._self(),
                                 right=self._conv(other),
                                 to=EqualFeature)

  def __ne__(self, other):
    return (self == other).flip_bool()

  def __add__(self, other):
    from declafe.feature_gen.binary import AddFeature
    return self._bc().make(left=self._self(),
                           right=self._conv(other),
                           to=AddFeature)

  def __sub__(self, other):
    from declafe.feature_gen.binary import SubFeature

    return self._bc().make(self._self(), self._conv(other), SubFeature)

  def __mul__(self, other):
    from declafe.feature_gen.binary import ProductFeature

    return self._bc().make(self._self(), self._conv(other), ProductFeature)

  def __mod__(self, other):
    from declafe.feature_gen.binary import ModFeature

    return self._bc().make(self._self(), self._conv(other), ModFeature)

  def __truediv__(self, other: "FeatureGen") -> "FeatureGen":
    from .binary.ops import DivideFeature

    return self._bc().make(self._self(), self._conv(other), DivideFeature)

  def __gt__(self, other):
    from declafe.feature_gen.binary import IsGreaterFeature

    return self._bc().make(self._self(), self._conv(other), IsGreaterFeature)

  def __lt__(self, other):
    from declafe.feature_gen.binary import IsLessFeature

    return self._bc().make(self._self(), self._conv(other), IsLessFeature)

  def __ge__(self, other):
    from declafe.feature_gen.binary import GEFeature

    return self._bc().make(self._self(), self._conv(other), GEFeature)

  def __le__(self, other):
    from declafe.feature_gen.binary import LEFeature

    return self._bc().make(self._self(), self._conv(other), LEFeature)

  def __and__(self, other):
    from declafe.feature_gen.binary.ops.AndFeature import AndFeature

    return self._bc().make(self._self(), self._conv(other), AndFeature)

  def __or__(self, other):
    from declafe.feature_gen.binary.ops.OrFeature import OrFeature

    return self._bc().make(self._self(), self._conv(other), OrFeature)


