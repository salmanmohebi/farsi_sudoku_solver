import re
from os.path import join, dirname
from setuptools import setup, find_packages

# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)


dependencies = [
    'opencv-python',
    'numpy'
]

setup(
    name='farsi_sudoku_solver',
    version=package_version,
    author='Salman Mohebi',
    author_email='s.mohebi22@gmail.com',
    install_requires=dependencies,
    packages=find_packages(),
)
