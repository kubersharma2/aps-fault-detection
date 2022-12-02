from setuptools import find_packages, setup
from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements() ->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_List = requirement_file
        requirement_List = 

setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="kubersharma002@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),


)