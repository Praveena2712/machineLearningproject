from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = [
            line.strip()
            for line in file_obj
            if line.strip() and line.strip() != HYPEN_E_DOT
        ]

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="praveena",
    author_email="praveenareethu@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)