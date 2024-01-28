from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.model_training import ModelTraining
from mlflow_project import logger

STAGE_NAME = 'Model Training Stage'


class ModelTrainingPipeline:
      def __init__(self):
            pass
      
      def main(self):
        try:
            config=ConfigurationManager()
            # print(config)
            model_training_config=config.get_model_training_config()
            model_training = ModelTraining(model_training_config)
            model_training.train()
        except Exception as e:
            raise e
        
if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        raise e