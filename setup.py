from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
  name='django-zcodes',
  version='1.0.0',

  description='A sample Python project',
  long_description="Django data model for zip codes in GeoDjango with preloaded data for the US.",
  url='https://github.com/pypa/sampleproject',
  author='Paul Bailey',
  author_email='paul.m.bailey@gmail.com',
  
  license='MIT',
  
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
  ],
  
  keywords='django geodjango zip codes',

  packages=find_packages(),
  
  install_requires=[],

  extras_require={
    'dev': [],
    'test': [],
  },
  
  data_files=[('zcode/fixtures', ['zcode/fixtures/zcodes_us.json'])],
)