#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
import sys

with open("README.md", "rb") as fh:
    long_description = fh.read()

extras = {
    'docs': ['sphinx'],
    'matrices': ['numpy'],
    'matplotlib': ['matplotlib'],
    'quantities': ['quantities', 'numpy'],
    'testing': ['flake8<3.0.0', 'pep8-naming==0.8.2',
                'flake8_docstrings==1.3.0', 'pycodestyle==2.0.0',
                'pydocstyle==3.0.0', 'pyflakes==1.2.3', 'nose', 'flake8-putty',
                'coverage'],
    'convert_to_py2': ['3to2', 'future>=0.15.2'],
}

setup(
    name="bone-pytex",
    version="0.1.5.a",
    keywords=("LaTex", "MarkDown"),
    description="一个用来简化LaTex编写的python库",
    long_description="一个用来简化LaTex编写的python库",
    license="GPL-3.0 Licence",
    url="https://github.com/tczrr1999/PyTex",
    author="zrr",
    author_email="2742392377@qq.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=['sympy', 'ordered-set', 'markdown', 'mistune'],
    extras_require=extras,
    scripts=[],
    # entry_points={
    #     'console_scripts': [
    #         'test = test.help:main'
    #     ]
    # }
)
