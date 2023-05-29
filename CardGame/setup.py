import os

from setuptools import find_packages, setup

cwd = os.path.dirname(os.path.abspath(__file__))

setup(
    name="CardGame",
    version="0.0.1",
    author="AbaoYang",
    author_email="jiunyi.yang.abao@gmail.com",
    description="CardGame Library of Waterball Course",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.8"
)
