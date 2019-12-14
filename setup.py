import os
import io
from setuptools import setup, find_packages


# Helpers
def read(*paths):
    """Read a text file."""
    basedir = os.path.dirname(__file__)
    fullpath = os.path.join(basedir, *paths)
    contents = io.open(fullpath, encoding='utf-8').read().strip()
    return contents


# Prepare
PACKAGE = 'referencer'
INSTALL_REQUIRES = [
    'pydoc-markdown',
    'click',
]
TESTS_REQUIRE = [
    'mock',
    'pylama',
    'pytest',
    'pytest-cov',
]
README = read('README.md')
VERSION = read(PACKAGE, 'VERSION')
PACKAGES = find_packages(exclude=['examples', 'tests'])


# Run
setup(
    name=PACKAGE,
    version=VERSION,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require={
        'develop': TESTS_REQUIRE,
    },
    entry_points={
        'console_scripts': [
            'referencer = referencer.__main__:cli',
        ]
    },
    zip_safe=False,
    long_description=README,
    long_description_content_type='text/markdown',
    description='Generate a markfown reference from your public API docstrings and add it to your readme',
    author='Evgeny Karev',
    author_email='eskarev@gmail.com',
    url='https://github.com/roll/referencer-py',
    license='MIT',
    keywords=[
        'docstring',
        'markdown',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
