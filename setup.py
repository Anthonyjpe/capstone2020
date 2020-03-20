
from setuptools import setup, find_packages

setup(
    name="c20_server",
    packages=find_packages('src'),
    package_dir={'': 'src'}
)

setup(
    name="c20_client",
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
