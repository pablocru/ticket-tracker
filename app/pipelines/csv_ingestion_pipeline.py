import logging
import time

import pandas as pd

from app.services.csv_reader import CSVReaderService

logger = logging.getLogger(__name__)


class CSVIngestionPipeline:
    def __init__(
        self,
        reader: CSVReaderService,
    ) -> None:

        self._reader = reader

    def run(self) -> pd.DataFrame:
        logger.info("Starting CSV ingestion pipeline")

        start = time.time()
        df = self._reader.read_latest()
        duration = time.time() - start
        read_rows = df.shape[0]

        logger.info("CSV loaded successfully")
        logger.debug("Read %d rows in %.2fs", read_rows, duration)

        return df
