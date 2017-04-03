from setuptools import setup
import versioneer


setup(
    name='doct',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Brookhaven National Laboratory',
    license='BSD 3-Clause',
    packages=['doct'],
    description='A read-only dottable dictionary',
    url='http://github.com/NSLS-II/doct',
    install_requires=['six', 'humanize', 'prettytable']
)
