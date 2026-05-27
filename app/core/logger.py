import logging
from logging.handlers import RotatingFileHandler

from app.config.logging_config import LoggingConfig


def configure_logging(config: LoggingConfig) -> None:
    config.file_handler.directory.mkdir(parents=True, exist_ok=True)

    root_logger = logging.getLogger()
    root_logger.setLevel(config.log_level)

    if root_logger.handlers:
        return

    console_handler = logging.StreamHandler()
    console_handler.setLevel(config.console_handler.log_level)
    console_handler.setFormatter(
        logging.Formatter(
            fmt=config.console_handler.log_format, datefmt=config.date_format
        )
    )

    file_handler = RotatingFileHandler(
        filename=config.file_handler.path,
        maxBytes=config.file_handler.max_bytes,
        backupCount=config.file_handler.backup_count,
        encoding=config.file_handler.encoding,
    )
    file_handler.setLevel(config.file_handler.log_level)
    file_handler.setFormatter(
        logging.Formatter(
            fmt=config.file_handler.log_format, datefmt=config.date_format
        )
    )

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
