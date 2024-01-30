from mlflow_project import logger
from mlflow_project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlflow_project.pipeline.stage_02_data_validation import DataValidationPipeline
from mlflow_project.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlflow_project.pipeline.stage_04_model_training import ModelTrainingPipeline
from mlflow_project.pipeline.satge05_model_evaluation import ModelEvaluationPipeline

logger.info('Welcome to the Second logging')

try:
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as e:
    logger.exception(e)

logger.info('Welcome to the Third logging')

try:
    data_validation = DataValidationPipeline()
    data_validation.main()
except Exception as e:
    logger.exception(e)

logger.info('Welcome to the Fourth logging')

try:
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
except Exception as e:
    logger.exception(e)


logger.info('Welcome to the Fifth logging')

try:
    model_training = ModelTrainingPipeline()
    model_training.main()
except Exception as e:
    logger.exception(e)


logger.info('Welcome to the Sixth logging')

try:
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
except Exception as e:
    logger.exception(e)

