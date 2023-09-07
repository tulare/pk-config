from setuptools import setup

def readme() :
    with open('README.md') as f :
        return f.read()

def license() :
    with open('LICENSE') as f:
        return f.read()

# Get version without import module
with open('src/pk_config/version.py') as f :
    exec(compile(f.read(), 'pk_config/version.py', 'exec'))

setup(
    name='pk-config',
    version=__version__,
    description='Configuration management for python projects',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Topic :: Utilities :: Configuration',
    ],
    keywords='python utilities configuration database',
    url='https://github.com/tulare/pk-config',
    author='Tulare Regnus',
    author_email='tulare.paxgalactica@gmail.com',
    license=license(),
    package_dir={'pk_config' : 'src/pk_config'},
    packages=['pk_config'],
    package_data={'pk_config' : []},
    include_package_data=True,
    install_requires=[
        "pathlib; python_version <= '2.7'"
    ],
    scripts=[],
    entry_points={
        'console_scripts' : [],
    },
    data_files=[
    ],
    test_suite='nose2.collector.collector',
    tests_require=['nose2'],
    zip_safe=False
)


