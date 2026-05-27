import logging

from app.config.logging_config import LoggingConfig
from app.core.logger import configure_logging

logger = logging.getLogger(__name__)


def main() -> None:
    logger_config = LoggingConfig()
    configure_logging(logger_config)

    logger.info("Hello, TicketTracker!")
    logger.debug("Hello, Debugger!")


if __name__ == "__main__":
    main()
