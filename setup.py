from setuptools import find_packages, setup
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy as np

extensions = Extension("module", ["module.c"], include_dirs=[np.get_include()]),

setup(
    name='BatchCorrection',
    packages=find_packages(include=['module']),
    version='0.1.0',
    ext_modules = cythonize(extensions)
)