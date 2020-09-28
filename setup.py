#!/usr/bin/env python3
# Roger Volden

from setuptools import setup
from setuptools import find_packages
from Cython.Build import cythonize

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='conk-rvolden',
    version='1.0',
    author='Roger Volden',
    author_email='rvolden@ucsc.edu',
    description='A modified SW aligner for C3POa',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rvolden/conk',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    setup_requires=['cython'],
    ext_modules=cythonize("conk/conk.pyx",
                          annotate=True),
)
