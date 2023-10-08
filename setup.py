from setuptools import find_packages, setup # Finding packages

from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]: # A function to read requirement.txt and return as list to be installed

    """
    This function will return the list of requirements

    """

    # requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) # We need th -e . to let requirement.txt to trigger setup.py. However we dont need to install it. Hence we remove it from the list

    return requirements




setup(

    name  = 'mlproject',
    version = '0.0.1',
    author = 'Nazir',
    author_email = 'Nazir.Zuberu@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),

)