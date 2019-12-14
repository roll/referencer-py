import click
from .document import generate_document
from . import config


# Module API

@click.command(help='')
@click.argument('package')
@click.argument('document')
@click.option('--in-place', is_flag=True, show_default=True)
@click.option('--package-pattern', default=config.PACKAGE_PATTERN, show_default=True)
@click.option('--document-section', default=config.DOCUMENT_SECTION, show_default=True)
@click.version_option(config.VERSION, message='%(version)s')
def cli(package, document, **options):
    """ Command-line interface

    ```
    Usage: referencer [OPTIONS] PACKAGE DOCUMENT

    Options:
      --in-place               [default: False]
      --package-pattern TEXT   [default: from \\.(\\w+) import (\\w+)]
      --document-section TEXT  [default: ## Reference]
      --version                Show the version and exit.
      --help                   Show this message and exit.
    ```

    """
    in_place = options.pop('in_place')
    content = generate_document(package, document, **options)
    if in_place:
        with open(document, 'w') as file:
            file.write(content)
            return
    print(content)
