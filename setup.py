import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name = 'spoken2written',
      packages = ['spoken2written'],
      version='0.1',
      license=open('License.txt').read(),
      description='Convert Spoken English given as text to Written English',
      author='Gaurav Kavhar',
      author_email='gauravkavhar304@gmail.com',
      url='https://github.com/GK4444/spoken2written-english',
      classifiers = [
     					'Intended Audience :: Developers',
      					'Programming Language :: Python'
  				],
	  long_description=open_file('README.md').read()

     )