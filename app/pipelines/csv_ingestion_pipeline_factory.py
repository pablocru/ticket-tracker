from app.config.csv_config import CSVConfig
from app.pipelines.csv_ingestion_pipeline import CSVIngestionPipeline
from app.services.csv_reader import CSVReaderService


def create_csv_ingestion_pipeline() -> CSVIngestionPipeline:
    csv_config = CSVConfig()
    reader = CSVReaderService(csv_config)

    return CSVIngestionPipeline(reader)
