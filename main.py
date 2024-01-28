from mlflow_project import logger
from mlflow_project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlflow_project.pipeline.stage_02_data_validation import DataValidationPipeline
from mlflow_project.pipeline.stage_03_data_transformation import DataTransformationPipeline

logger.info('Welcome to the Second logging')

try:
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as e:
    logger.exception(e)


try:
    data_validation = DataValidationPipeline()
    data_validation.main()
except Exception as e:
    logger.exception(e)


try:
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
except Exception as e:
    logger.exception(e)


