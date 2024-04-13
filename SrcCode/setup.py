from setuptools import setup
import setuptools
setup(
    name='PyLibBass',
    version='1.0',
    author_email='riritoninigaya@hotmail.com',
    author='Ririto Ninigaya',
    license='MIT License,
    url='https://github.com/RiritoNinigaya/LibPyBass',
    description='My First Library For BASS(WORKS ONLY X64!!!)',
    packages=setuptools.find_packages(),
    package_data={
        '': ['x64_bass\\*.dll'],
    }
)
