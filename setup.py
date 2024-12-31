from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="image_to_mesh",
    version="0.0.1",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "image_to_mesh = image_to_mesh:main"
        ]
    }
)