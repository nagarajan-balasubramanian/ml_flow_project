from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_url:str
    local_file:Path
    unzip_dir:Path

@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    unzip_dir:Path
    all_schema:dict

@dataclass
class DataTransformationConfig:
    root_dir:Path
    data_dir:Path


@dataclass
class ModelTrainingConfig:
    root_dir:Path
    train_data:Path
    test_data: Path
    model_name: str
    alpha : float
    l1_ratio : float
    target_column :str


@dataclass
class ModelEvaluationConfig:
    root_dir:Path
    test_data: Path
    model_name: Path
    metric_file :Path
    all_params : dict
    target_column :str