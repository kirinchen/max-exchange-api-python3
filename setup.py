import os

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="max_exchange_api_python3",
    version=os.getenv('Version', '0.0.0'),
    author="Kirin",
    author_email="kirin.chen1985@gmail.com",
    description="max_exchange_api_python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True,
    packages=find_packages()
)
