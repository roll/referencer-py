from . import config
__version__ = config.VERSION


# Module API

from .cli import cli
from .document import generate_document
from .reference import generate_reference
