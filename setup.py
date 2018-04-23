'''
Created on 08.02.2016

@author: tklingenberg
'''

from setuptools import setup, find_packages

setup(
    # Application name:
    name='MeMoDB',

    # Version number (initial):
    version='0.1.0',

    # Short desription of the project:
    description='Common DB access for MeMoBuilder and MeMoSim',

    # Application author details:
    author='Thole Klingenberg',
    autor_email='thole.klingenberg@offis.de',

    # Packages
    packages=find_packages(),

    include_package_data=True,

    classifiers=[
        'Private :: Do Not Upload',
    ],

    install_requires=[
        'h5py',
        'pyyaml',
    ],
)