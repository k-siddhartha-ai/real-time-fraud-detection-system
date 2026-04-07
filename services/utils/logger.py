"""
Industry-ready logger utility
No duplicate logs
Reusable across services
"""

import logging
from functools import lru_cache


@lru_cache
def get_logger(name: str) -> logging.Logger:
    """
    Returns configured logger.
    Uses cache to avoid duplicate handlers.
    """

    logger = logging.getLogger(name)

    if not logger.handlers:   # Prevent duplicate logs
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.propagate = False

    return logger
