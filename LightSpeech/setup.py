import os
import unittest
from setuptools import setup, find_packages


def discover_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("test", pattern="test_*.py")
    return test_suite


def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, mode="r", encoding="utf-8") as f:
        return f.read()


setup(
    name="msft-lightspeech",
    description="",
    author="Dmitry Kryuchkov",
    packages=find_packages(),
    install_requires=read("requirements.txt").splitlines(),
    zip_safe=True,
)
