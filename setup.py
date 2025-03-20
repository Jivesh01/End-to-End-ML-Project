from setuptools import setup, find_packages
from typing import List

hypen_e_dot = '-e .'

def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',' ') for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Jivesh',
    author_email='jiveshbharambe04@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt'),
)