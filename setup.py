# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

# Get version without import module
exec(compile(open('pk_config/version.py').read(),
             'pk_config/version.py', 'exec'))

with open('README.md') as f :
    readme = f.read()

with open('LICENSE') as f :
    license = f.read()

setup(
    name='pk-config',
    version=__version__,
    description='Configuration management for python projects',
    long_description=readme,
    author='Tulare Regnus',
    author_email='tulare.paxgalactica@gmail.com',
    url='https://github.com/tulare/pk-config',
    license=license,
    packages=find_packages(exclude=('tests',)),
    zip_safe=False,
    #install_requires=[defined in setup.cfg]
)
