import click
from .document import generate_document
from . import config


# Module API

@click.command()
@click.argument('package')
@click.argument('document')
@click.option('--in-place', is_flag=True)
@click.option('--package-pattern', default=config.PACKAGE_PATTERN)
@click.option('--document-section', default=config.DOCUMENT_SECTION)
@click.version_option(config.VERSION, message='%(version)s')
def cli(package, document, **options):
    """ Command-line interface
    """
    in_place = options.pop('in_place')
    content = generate_document(package, document, **options)
    if in_place:
        with open(document, 'w') as file:
            file.write(content)
            return
    print(content)
