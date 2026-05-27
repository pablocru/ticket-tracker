from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CSVConfig:
    input_directory: Path = Path("data/input")
    file_pattern: str = "*.csv"
    encoding: str = "utf-8"
    separator: str = ","
