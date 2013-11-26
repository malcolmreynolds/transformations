from setuptools import setup, Extension
import numpy

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='transformations',
      author='Christoph Gohlke',
      description="Homogeneous Transformation Matrices and Quaternions.",
      license='BSD',
      version='2013.06.29',
      packages=['transformations'],
      long_description=read('README.md'),
      install_requires=['numpy', 'cython'],
      ext_modules=[Extension('transformations._transformations', ['transformations/transformations.c'],
                             include_dirs=[numpy.get_include()])])
