from mlflow_project.utils.common import read_yaml, create_directories
from mlflow_project.constants import *
from mlflow_project.entity.config_entity import *
import json

class ConfigurationManager:
    def __init__(
            self,
            config_file_path = CONFIG_FILE_PATH, 
            param_file_path = PARAMS_FILE_PATH,
            schema_file_path = SCHEMA_FILE_PATH):

            self.config=read_yaml(config_file_path)
            self.schema=read_yaml(schema_file_path)
            self.params=read_yaml(param_file_path)

            print(type(self.config))
            create_directories([self.config['artifacts_root']])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
          config= self.config['data_ingestion']
        #     print(config)
          create_directories([config['root_dir']])
          
          data_ingestion_config = DataIngestionConfig(
                root_dir =config['root_dir'],
                source_url = config['source_url'],
                local_file = config['local_file'],
                unzip_dir = config['unzip_dir'])
          return data_ingestion_config
                

    def get_data_validation_config(self) -> DataValidationConfig:
                  config= self.config['data_validation']
                  print(config['unzip_data_dir'])
                  schema= self.schema['COLUMNS']
                  create_directories([config['root_dir']])

                  data_validation_config = DataValidationConfig(
                        root_dir =config['root_dir'],
                        STATUS_FILE = config['STATUS_FILE'],
                        unzip_dir = config['unzip_data_dir'],
                        all_schema = schema)
                  return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
                  config= self.config['data_transformation']
                  create_directories([config['root_dir']])
                  
                  data_transformation_config = DataTransformationConfig(
                        root_dir =config['root_dir'],
                        data_dir = config['data_dir'])
                  return data_transformation_config

    def get_model_training_config(self) -> ModelTrainingConfig:
                  config= self.config['model_training']
                  #print(config['unzip_data_dir'])
                  target_column= self.schema['TARGET_COLUMN']
                  create_directories([config['root_dir']])
                  params=self.params['ElasticNet']

                  model_training_config = ModelTrainingConfig(
                        root_dir =config['root_dir'],
                        train_data= config['training_data'],
                        test_data = config['test_data'],
                        model_name = config['model_name'],
                        alpha=params['alpha'],
                        l1_ratio=params['l1_ratio'],
                        target_column=target_column)

                  return model_training_config
