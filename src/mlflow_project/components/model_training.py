from mlflow_project import logger
from mlflow_project.config.configuration import ModelTrainingConfig
import pandas as pd
from sklearn.linear_model import ElasticNet 
import os
import joblib

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config =config

    def train(self):
        train_data = pd.read_csv(self.config.train_data)
        test_data = pd.read_csv(self.config.test_data)

        # print(self.config.target_column)
        # print(self.config.alpha)
        # print(self.config.l1_ratio)
        train_x = train_data.drop([self.config.target_column['name']],axis=1)
        test_x = test_data.drop([self.config.target_column['name']],axis=1)

        train_y=train_data[self.config.target_column['name']]
        test_y=test_data[self.config.target_column['name']]

        lr=ElasticNet(alpha=float(self.config.alpha),l1_ratio=float(self.config.l1_ratio),random_state=42)
        lr.fit(train_x,train_y)
        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))


