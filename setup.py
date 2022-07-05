from os import path
from setuptools import setup, find_packages

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README = f.read()

setup(
    name='sophos_central_siem_integration',
    version="2.1.0",
    packages=[
        "sophos_central_siem_integration",
        "sophos_central_siem_integration.tests",
        "sophos_central_siem_integration.tests.unit",
    ],
    description='Sophos Central SIEM Integration',
    long_description=README,
    author='Sophos Central',
    author_email='contact@sophos.com',
    url='https://github.com/sophos/Sophos-Central-SIEM-Integration',
    include_package_data=True,
    license='Apache',
    dependency_links=[],
    install_requires=[
        "mock",
        "configparser",
        "pathlib",
        "requests",
        "config",
        "logging",
        "pycef"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
