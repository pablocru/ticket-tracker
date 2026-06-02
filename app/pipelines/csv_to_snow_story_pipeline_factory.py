from app.config.csv_config import CSVConfig
from app.integrations.service_now.story_mapper import ServiceNowStoryMapper
from app.pipelines.csv_to_snow_story_pipeline import CSVToSnowStoryPipeline
from app.services.csv_reader import CSVReaderService


def create_csv_to_snow_story_pipeline() -> CSVToSnowStoryPipeline:
    csv_config = CSVConfig()
    reader = CSVReaderService(csv_config)
    mapper = ServiceNowStoryMapper()

    return CSVToSnowStoryPipeline(reader, mapper)
