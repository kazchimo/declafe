from typing import Union

import numpy
import pandas as pd

from declafe.feature_gen.ComposedFeature import *
from declafe.feature_gen.ConstFeature import *
from declafe.feature_gen.Features import *
from declafe.feature_gen.dsl import *
from .feature_gen.FeatureGen import *

series = Union[pd.Series, numpy.ndarray]

__all__ = ["feature_gen", "agg_feature_gen", "astype"]
