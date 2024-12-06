from setuptools import setup, find_packages

setup(
    name='crime_test',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    description='A package to validate and compute statistics on crime data',
    author='Your Name',
    author_email='your.email@example.com',
)

