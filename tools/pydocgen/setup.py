from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pydocgen',
    version='0.1.0',
    description='Tool for generating Pulumi Python documentation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pulumi/docs',
    author='Sean Gillespie',
    author_email='sean@pulumi.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        "sphinx>=1.8.3",
        "Jinja2>=2.10",
        "m2r>=0.2.1"
    ],
    entry_points={
        'console_scripts': [
            'pydocgen=pydocgen:main',
        ],
    },
)
