from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='mypackage',
      version=version,
      description="20210518",
      long_description="""\
20210518""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='blog',
      author='hitzhu',
      author_email='',
      url='',
      license='license',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
