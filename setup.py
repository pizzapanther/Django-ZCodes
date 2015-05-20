from setuptools import setup, find_packages

setup(
  name = "django-zcodes",
  version = '1.0.0',
  description = "Django data model for zip codes in GeoDjango with preloaded data for the US.",
  url = "https://github.com/pizzapanther/Django-ZCodes",
  author = "Paul Bailey",
  author_email = "paul.m.bailey@gmail.com",
  license = "MIT",
  packages = ['zcodes', 'zcodes.migrations'],
  include_package_data = True,
  data_files=[('zcodes/fixtures', ['zcodes/fixtures/zcodes_us.json'])],
  
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
  ],
)
