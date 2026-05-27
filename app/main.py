import logging
import time

from app.config.csv_config import CSVConfig
from app.config.logging_config import LoggingConfig
from app.core.logger import configure_logging
from app.services.csv_reader import CSVReaderService

logger = logging.getLogger(__name__)


def main() -> None:
    logger_config = LoggingConfig()
    configure_logging(logger_config)

    logger.info("Starting CSV ingestion process")

    csv_config = CSVConfig()
    reader = CSVReaderService(csv_config)

    try:
        start = time.time()
        df = reader.read_latest()
        duration = time.time() - start
        logger.info(
            "Successfully read %d tickets in %.2fs",
            df.shape[0],
            duration,
        )

    except Exception as e:
        logger.error("Error while reading CSV: %s", str(e))
