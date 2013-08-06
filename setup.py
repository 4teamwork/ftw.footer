from setuptools import setup, find_packages
import os

version = '1.1.3.dev0'

maintainer = 'Mathias Leimgruber'

tests_require = [
    'plone.app.testing',
    'ftw.builder',
    ]

setup(name='ftw.footer',
      version=version,
      description="Show 1 - 4 portlets as footer",
      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers

      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

      keywords='plone ftw viewlet footer',
      author='4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='https://github.com/4teamwork/ftw.footer',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
# -*- Entry points: -*-
[z3c.autoinclude.plugin]
target = plone
""",
      )