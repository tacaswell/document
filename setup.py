from setuptools import setup
import versioneer


setup(
    name='doct',
    version=versioneer.get_version(),
    author='Brookhaven National Laboratory',
    license='BSD 3-Clause',
    py_modules=['doct'],
    description='A read-only dottable dictionary',
    url='http://github.com/NSLS-II/doct',
    install_requires=['six', 'humanize', 'prettytable']
)
