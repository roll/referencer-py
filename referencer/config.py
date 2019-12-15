import io
import os


# Module API

PACKAGE_PATTERN = r'from \.(\w+) import (\w+)'
DOCUMENT_SECTION = '## API Reference'
VERSION = io.open(os.path.join(os.path.dirname(__file__), 'VERSION')).read().strip()
