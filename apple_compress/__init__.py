from importlib.metadata import version

from .compress import compress, decompress  # noqa: F401
from .types import Algorithm  # noqa: F401

__version__ = version(__package__)
