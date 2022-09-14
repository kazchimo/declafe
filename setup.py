import setuptools
from setuptools import setup
from codecs import open
from os import path

VERSION = "0.0.13"

package_name = "declafe"
root_dir = path.abspath(path.dirname(__file__))

def _requirements():
  return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]

with open('README.md', encoding='utf-8') as f:
  long_description = f.read()

setup(
  name=package_name,
  version=VERSION,
  description='Declarative feature generation library',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/kazchimo/declafe',
  author='kazchimo',
  author_email='kazchimo@gmail.com',
  license='MIT',
  keywords='machine learning, declarative, feature generation',
  packages=setuptools.find_packages(),
  install_requires=_requirements(),
  classifiers=[
    "Programming Language :: Python :: 3.10"
  ],
)
