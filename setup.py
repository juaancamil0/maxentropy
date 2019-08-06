#!/usr/bin/env python

import io
import re

from setuptools import setup

with io.open("maxentropy/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)


setup(
    name='maxentropy',
    version = '0.3.0',
    packages=['maxentropy'],
    package_data={
        '': ['*.txt', '*.rst', '*.md'],
        'examples': ['*.py'],
        'notebooks': ['*.ipynb']
    },
    author='Ed Schofield',
    author_email='ed@pythoncharmers.com',
    description='Maximum entropy and minimum divergence models in Python',
    license='BSD',
    keywords='maximum-entropy minimum-divergence kullback-leibler-divergence KL-divergence bayesian-inference bayes scikit-learn sklearn prior prior-distribution',
    url='https://github.com/PythonCharmers/maxentropy.git',
    install_requires=['sklearn'],
    python_requires=">=3.3",
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering']
)

