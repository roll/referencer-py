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
            command = 'pydocmd simple %s.%s++' % (package, module)
            code, docs = subprocess.getstatusoutput(command)
            if code != 0:
                raise Exception(docs)
            docs = re.sub(r'\n\n-', r'\n-', docs)
            docs = re.sub(r'\\:', r':', docs)
            if docs.find('## %s' % object) == -1:
                docs = docs.replace('# %s' % object, '## %s' % object)
            block = ''
            for docline in docs.split("\n"):
                if docline.startswith('## '):
                    if capture:
                        break
                if docline == '## %s' % object:
                    capture = True
                if not capture:
                    continue
                if is_class:
                    docline = re.sub(r'^### (.*)', r'### %s.\1' % object.lower(), docline)
                    docline = re.sub(r'^%s\.' % object, r'%s.' % object.lower(), docline)
                docline = re.sub(r'^(###?) ([\w.]+)', r'#\1 `\2`', docline)
                block += "%s\n" % docline
            if not block:
                raise Exception('No docs for: %s' % line)
            content += block
    return content
