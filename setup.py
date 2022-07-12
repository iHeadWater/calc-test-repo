#!/usr/bin/env python

import os
import sys
import random
import string

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='calc-test-repo',
    version=''.join(random.sample(string.digits, 8)),
    description='A test project',
    long_description='https://readthedocs.org/projects/calctest/',
    author='CALC_TEMPLATE',
    url='https://github.com/iHeadWater/calc-test-repo',
    packages=[
        'calc-test-repo',
    ],
    package_dir={'calc-test-repo': 'calc-test-repo'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='calc-test-repo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
