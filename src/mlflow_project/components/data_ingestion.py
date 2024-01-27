import os
import urllib.request as request
import zipfile
from mlflow_project.utils.common import get_size
from mlflow_project.config.configuration import DataIngestionConfig
from mlflow_project import logger
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
            self.config = config
            # print(config)

    def download_file(self):
        if not os.path.exists(self.config.local_file):
             filename,header=   request.urlretrieve(
                url=self.config.source_url,
                filename = self.config.local_file
                )
             logger.info(f'Downloaded the file {filename} Successfully')
        else:
              logger.info(f"File already downloaded and size of file is : \
                          {get_size(Path(self.config.local_file))}")
          
                
    def extract_zip_file(self):
          unzip_path = self.config.unzip_dir
          os.makedirs(unzip_path,exist_ok=True)
          with zipfile.ZipFile(self.config.local_file,'r') as zip_file_content:
                zip_file_content.extractall(unzip_path)