from importlib.metadata import version

from loguru import logger as _logger

from .compress import compress, decompress  # noqa: F401
from .types import Algorithm  # noqa: F401

__version__ = version(__package__)
_logger.disable(__package__)
