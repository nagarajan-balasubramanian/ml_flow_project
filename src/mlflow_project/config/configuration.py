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

            # print(type(self.config))
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
                