from setuptools import find_packages,setup
from typing import List

Hypen_E_dot='-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if Hypen_E_dot in requirements:
        requirements.remove(Hypen_E_dot)
    return requirements

setup(
    name='Fault detection',
    version='0.0.1',
    author='Raj Kewat',
    author_email='rajkewat@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)