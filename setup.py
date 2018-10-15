import re
from os.path import join, dirname
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'sudoku', '__init__.py')) as v_file:
    package_version = re.compile(
        r'.*__version__=\'(.*?)\'', re.S
    ).match(v_file.read()).group(1)

dependencies = ['cv2', 'numpy']

setup(
    name='farsi_sudoku_solver',
    version=package_version,
    author='Salman Mohebi',
    author_email='s.mohebi22@gmail.com',
    install_requires=dependencies,
    packages=find_packages(),

)
