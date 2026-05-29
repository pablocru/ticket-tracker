import logging

from app.config.logging_config import LoggingConfig
from app.core.logger import configure_logging
from app.pipelines.csv_ingestion_pipeline_factory import create_csv_ingestion_pipeline

logger = logging.getLogger(__name__)


def main() -> None:
    logger_config = LoggingConfig()
    configure_logging(logger_config)

    pipeline = create_csv_ingestion_pipeline()

    try:
        pipeline.run()
    except Exception:
        logger.exception("ETL failed")
