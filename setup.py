from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
    name="covid19-estimator-py", 
    version="1.0",
    author="Daniel Kamar",
    author_email="dan@koitoror.ml",
    description="A covid19-estimator online tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://cov-19-ke.herokuapp.com",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
