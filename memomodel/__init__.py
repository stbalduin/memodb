import yaml

import h5db

from memomodel.memo_objects import SimConfig, VirtualState, ModelStructure, SamplerConfig, ParameterVariation, \
    ParameterVariationMode, StrategyConfig, KeyValuePair, KeyObjectPair, ApproximationFunctionConfig, \
    SurrogateModelConfig, InputResponseDataset, TrainingResult, DatasetOwnership, SurrogateModelTrainingResult, \
    SurrogateModel
from memomodel.memo_objects import MeMoDB

from memomodel.memo_objects import SimulationModelDescription, OLSModelDescription, \
    KernelRidgeRegressionModelDescription, GenericModelDescription
from memomodel.memo_objects import MeMoSimDB

h5db.core.register_h5db_yaml_objects()
