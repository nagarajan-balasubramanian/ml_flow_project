from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.data_ingestion import DataIngestion
from mlflow_project import logger

STAGE_NAME = 'Data Ingestion Stage'


class DataIngestionPipeline:
      def __init__(self):
            pass
      
      def main(self):
        try:
            config=ConfigurationManager()
            print(config)
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        
if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        raise e