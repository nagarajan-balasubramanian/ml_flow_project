from mlflow_project import logger
from mlflow_project.pipeline.stage_01_data_ingestion import DataIngestionPipeline

logger.info('Welcome to the first logging')

try:
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as e:
    logger.exception(e)


