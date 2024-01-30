from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.model_evaluation import ModelEvaluation
from mlflow_project import logger

STAGE_NAME = 'Model Evaluation Stage'


class ModelEvaluationPipeline:
      def __init__(self):
            pass
      
      def main(self):
        try:
            config=ConfigurationManager()
            # print(config)
            model_evaluation_config=config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(model_evaluation_config)
            model_evaluation.run_mlflow()
        except Exception as e:
            raise e
        
if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        raise e