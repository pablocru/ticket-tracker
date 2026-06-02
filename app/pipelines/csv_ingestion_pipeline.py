import logging
from time import perf_counter

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

        start = perf_counter()

        df = self._reader.read_latest()

        logger.info(
            "CSV loaded (%d rows, %d columns) in %.3fs",
            len(df),
            len(df.columns),
            perf_counter() - start,
        )

        if df.empty:
            logger.warning("CSV is empty")

        return df
