
from setuptools import find_packages, setup

requirements_file = "requirements.txt"

with open("README.md") as f:
    readme = f.read()

setup(
    name="miner-manager",
    version="0.1.0",
    description="Package for managing crypto miner.",
    long_description=readme,
    author="Peter Begle",
    url="https://github.com/pbegle",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["miner_manager"],
    install_requires=open(requirements_file).readlines(),
    packages=find_packages(exclude=["tests"]),
)