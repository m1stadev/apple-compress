import sys
from importlib.metadata import version

from loguru import logger as _logger

from .compress import compress, decompress  # noqa: F401
from .types import Algorithm  # noqa: F401

__version__ = version(__package__)

_logger.remove()
_logger.add(
    sys.stderr,
    level='WARNING',
    format='[{time:MMM D YYYY - hh:mm:ss A zz}] {level} {module}:{line} {message}',
)
