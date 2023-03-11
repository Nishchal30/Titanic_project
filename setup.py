from setuptools import find_packages, setup

var = "-e ."

def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
         
        if var in requirements:
            requirements.remove(var)
    
    return requirements
      
setup(
name="End to end ML project on Titanic dataset",
author="Nishchal",
version="0.0,1",
author_email="nishchaljinturkar30@gmail.com",
packages=find_packages(),
install_requires = get_requirements('requirements.txt')



)