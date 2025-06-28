"""Simple helper to configure consistent timestamped logging across modules."""

import logging
import sys


def setup(name: str = __name__) -> logging.Logger:
    """Return a logger with ISO-8601 timestamps.

    The logger is configured only once per process. Subsequent calls will
    reuse the existing logger instance.
    """

    logger = logging.getLogger(name)

    # Avoid adding multiple handlers in interactive / dev sessions
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        # Default to INFO level; can be overridden by caller if needed
        logger.setLevel(logging.INFO)

    return logger 