import os.path
from setuptools import setup, find_packages, __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


exec (open('version.py').read())

setup(name='patchmind',
      version=__version__,
      description='patchmind project',
      long_description=read('README.md'),
      author='Pobear Wang',
      author_email='pobear@100tal.com',
      url='https://github.com/pobear/tornado-project-skeleton',
      include_package_data=True,
      classifiers=[],
      packages=find_packages(exclude=['tests']),
      install_requires=[
          'tornado==4.3',
          'motor==0.6.2',
      ],
      setup_requires=[
          'pytest-runner==2.6.2',
      ],
      tests_require=[
          'pytest==2.8.2',
          'pytest-pep8==1.0.6',
          'pytest-cov==2.2.0',
      ])
