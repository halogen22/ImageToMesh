from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="imageToStl",
    version="0.0.1",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "imageToStl = imageToStl:main"
        ]
    }
)