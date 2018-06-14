from setuptools import setup
import os


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="tensorflow-stubs",
    description="PEP 561 type stubs for tensorflow",
    url="https://www.tensorflow.org/",
    license="MIT",
    version="0.0.1",
    packages=["tensorflow-stubs"],
    # PEP 561 requires these
    install_requires=["tensorflow"],
    package_data=find_stubs("tensorflow-stubs"),
)
