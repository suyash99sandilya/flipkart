from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies,
    excluding editable installs like '-e .'.
    """
    requirement_list: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            requirement_list = [
                req.strip() for req in file.readlines() if req.strip() and not req.startswith("-e")
            ]
    except FileNotFoundError:
        print("requirements.txt not found. Please ensure the file exists.")

    return requirement_list


setup(
    name="flipkart",
    version="0.0.1",
    author="Suyash Sandilya",
    author_email="suyash99sandilya@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),  # Dynamically fetch requirements
)
