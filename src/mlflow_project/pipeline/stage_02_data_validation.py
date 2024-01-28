from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.data_validation import DataValidation
from mlflow_project import logger

STAGE_NAME = 'Data Validation Stage'


class DataValidationPipeline:
      def __init__(self):
            pass
      
      def main(self):
        try:
            config=ConfigurationManager()
            # print(config)
            data_validation_config=config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
        
if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        raise e