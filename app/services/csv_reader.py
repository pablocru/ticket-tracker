import pandas as pd

from app.config.csv_config import CSVConfig


class CSVReaderService:
    def __init__(self, config: CSVConfig):
        self._config = config

    def read_latest(self) -> pd.DataFrame:
        files = list(self._config.input_directory.glob(self._config.file_pattern))

        if not files:
            raise FileNotFoundError(
                f"No CSV files found in {self._config.input_directory}"
            )

        latest_file = max(files, key=lambda f: f.stat().st_mtime)

        return pd.read_csv(
            latest_file,
            sep=self._config.separator,
            encoding=self._config.encoding,
        )
