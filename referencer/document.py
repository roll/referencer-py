from .reference import generate_reference
from . import config


# Module API

def generate_document(package, document,
        package_pattern=config.PACKAGE_PATTERN,
        document_section=config.DOCUMENT_SECTION):
    """ Generate document
    """
    content = ''
    replace = False
    reference = generate_reference(package, package_pattern)
    with open(document) as file:
        for line in file:
            if line.startswith('%s ' % document_section.split(' ')[0]):
                if replace:
                    content += "\n%s" % reference
                replace = False
            if line.startswith(document_section):
                content += line
                replace = True
            if replace:
                continue
            content += line
        if replace:
            content += "\n%s" % reference
    return content
