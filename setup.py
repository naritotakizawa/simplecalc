import os
from setuptools import find_packages, setup
 
with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'rb') as readme:
    README = readme.read()
 
setup(
    name='simplecalc',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Simple Calculator by tkinter',
    long_description=README.decode(),
    url='https://github.com/naritotakizawa/simplecalc',
    author='Narito Takizawa',
    author_email='toritoritorina@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={'console_scripts': [
        'simplecalc = simplecalc.main:main',
    ]},
)