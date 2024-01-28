from mlflow_project import logger
from mlflow_project.config.configuration import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
import os

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config =config

    
    def train_test_split_process(self):
        data = pd.read_csv(self.config.data_dir)

        train , test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'))
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'))

        logger.info("Training and Testing data split completed")
        logger.info(train.shape)
        logger.info(test.shape)