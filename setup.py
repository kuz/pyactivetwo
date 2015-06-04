"""
pyactivetwo: Python library for reading signal from BioSemi ActiveTwo EEG device

Note that "python setup.py test" invokes pytest on the package. With appropriately
configured setup.cfg, this will check both xxx_test modules and docstrings.

Copyright 2015, Ilya Kuzovkin.
Licensed under MIT.
"""


import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # import here, because outside the required eggs aren't loaded yet
        sys.exit(pytest.main(self.test_args))


version = "0.1"

setup(name="pyactivetwo",
      version=version,
      description="Python library for reading signal from BioSemi ActiveTwo EEG device",
      long_description=open("README.rst").read(),
      classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python'
      ],
      keywords="eeg signal biosemi activetwo",  # Separate with spaces
      author="Ilya Kuzovkin",
      author_email="ilya.kuzovkin@gmail.com",
      url="http://github.com/kuz/pyactivetwo",
      license="MIT",
      packages=find_packages(exclude=['examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      install_requires=['numpy'],
)

