import logging
from time import perf_counter

from app.integrations.service_now.story_dto import ServiceNowStoryDTO
from app.integrations.service_now.story_mapper import ServiceNowStoryMapper
from app.services.csv_reader import CSVReaderService

logger = logging.getLogger(__name__)


class CSVToSnowStoryPipeline:
    def __init__(
        self,
        reader: CSVReaderService,
        mapper: ServiceNowStoryMapper,
    ) -> None:
        self._reader = reader
        self._mapper = mapper

    def run(self) -> list[ServiceNowStoryDTO]:
        logger.info("Starting CSV to ServiceNow story pipeline")

        start = perf_counter()

        df = self._reader.read_latest()

        logger.info(
            "CSV loaded (%d rows, %d columns)",
            len(df),
            len(df.columns),
        )

        if df.empty:
            logger.warning("CSV is empty, nothing to process")
            return []

        stories = self._mapper.to_dtos(df)

        logger.info(
            "Generated %d ServiceNow stories from %d products",
            len(stories),
            len({story.product for story in stories}),
        )

        logger.debug(
            "First generated story: %s",
            stories[0] if stories else None,
        )

        logger.info(
            "Pipeline completed in %.3fs",
            perf_counter() - start,
        )

        return stories
