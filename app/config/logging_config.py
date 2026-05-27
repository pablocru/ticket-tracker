import logging
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class ConsoleHandlerConfig:
    log_level: int = logging.DEBUG
    log_format: str = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


@dataclass(frozen=True)
class FileHandlerConfig:
    log_level: int = logging.INFO
    log_format: str = (
        "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
    )

    directory: Path = Path("data/logs")
    filename: str = "application.log"
    encoding: str = "utf-8"

    max_file_size_mb: int = 5
    backup_count: int = 5

    @property
    def max_bytes(self) -> int:
        return self.max_file_size_mb * 1024 * 1024

    @property
    def path(self) -> Path:
        return self.directory / self.filename


@dataclass(frozen=True)
class LoggingConfig:
    log_level: int = logging.DEBUG
    date_format: str = "%Y-%m-%dT%H:%M:%S"

    console_handler: ConsoleHandlerConfig = field(default_factory=ConsoleHandlerConfig)
    file_handler: FileHandlerConfig = field(default_factory=FileHandlerConfig)
