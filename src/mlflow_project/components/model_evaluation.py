from mlflow_project import logger
from mlflow_project.config.configuration import *
import pandas as pd
from sklearn.metrics import * 
import os
import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from mlflow_project.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual,pred):
        rmse=np.sqrt(mean_squared_error(actual, pred))
        mae=mean_absolute_error(actual,pred)
        r2=r2_score(actual,pred)
        return rmse,mae,r2

    def run_mlflow(self):
        test_data_path = self.config.test_data
        model_name_path = self.config.model_name

        test_data = pd.read_csv(test_data_path)
        model = joblib.load(model_name_path)

        print(self.config.target_column)
        test_data_x = test_data.drop([self.config.target_column['name']],axis=1)
        print(test_data_x)
        test_data_y = test_data[self.config.target_column['name']]

        predicted_quality = model.predict(test_data_x)

        (rmse,mae,r2) = self.eval_metrics(test_data_y, predicted_quality)

        scores = {"rmse": rmse, "mae": mae, "r2": r2}

        save_json(Path(self.config.metric_file),data=scores)


