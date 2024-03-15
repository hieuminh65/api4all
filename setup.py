import os

import setuptools

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

version = {}
with open(os.path.join(here, "api4all/version.py")) as fp:
    exec(fp.read(), version)
__version__ = version["__version__"]

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="api4all",
    version=__version__,
    author="Hieu Nguyen",
    author_email="hieung.tech@gmail.com",
    description="Easy-to-use LLM API from a state-of-the-art provider and comparison.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hieuminh65/api4all",
    packages=setuptools.find_packages(include=["api4all*"], exclude=["test"]),
    install_requires=requirements,
)