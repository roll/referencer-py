import re
import subprocess
from . import config


# Module API

def generate_reference(package,
        package_pattern=config.PACKAGE_PATTERN):
    """ Generate reference
    """
    content = ''
    with open('%s/__init__.py' % package) as file:
        for line in file:
            match = re.match(package_pattern, line)
            if not match:
                continue
            capture = False
            module, object = match.groups()
            is_class = object[0].isupper()
            docs = subprocess.getoutput('pydocmd simple %s.%s++' % (package, module))
            for line in docs.split("\n"):
                if line.startswith('## '):
                    capture = False
                if line == '## %s' % object:
                    capture = True
                if not capture:
                    continue
                if is_class:
                    line = re.sub(r'^### (.*)', r'### %s.\1' % object.lower(), line)
                    line = re.sub(r'^%s\.' % object, r'%s.' % object.lower(), line)
                line = re.sub(r'^(###?) ([\w.]+)', r'#\1 `\2`', line)
                content += "%s\n" % line
        #  headings = ''
        #  for heading in re.findall(r'### `(.*)`', content):
            #  headings += "- [`%s`](#%s)\n" % (heading, heading)
        #  content = "%s\n---\n\n%s" % (headings, content)
    return content
