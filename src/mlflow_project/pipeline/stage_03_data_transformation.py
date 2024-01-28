from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.data_transformation import DataTransformation
from mlflow_project import logger

STAGE_NAME = 'Data Transformation Stage'


class DataTransformationPipeline:
      def __init__(self):
            pass
      
      def main(self):
        try:
            config=ConfigurationManager()
            # print(config)
            data_transformation_config=config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.train_test_split_process()
        except Exception as e:
            raise e
        
if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        raise e