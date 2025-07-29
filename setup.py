from struct import pack
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """This function will return the list of requirements from the requirements.txt file"""

    requirement_lst: List[str] = []

    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()

                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Dhaivat NJ',
    author_email='dhaivat.jambudia@gmail.com',
    packages=find_packages(), # find_packages() will find all the packages in the project, all the folder with __init__.py file
    install_requires=get_requirements(),
)