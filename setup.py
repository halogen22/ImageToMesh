from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="imageTo3D",
    version="0.0.1",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "imageTo3D = imageTo3D:main"
        ]
    }
)