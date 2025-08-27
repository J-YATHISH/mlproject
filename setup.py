from setuptools import setup, find_packages
from typing import List


HYPEN_DOT = '-e .'
def get_requirements(file_path:str)->List:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements
        

setup(
    name='mlproject',
    version='0.1.0',
    author='Yathish',
    author_email='yathishj006@gmail.com',
    description='my ML pakage',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)