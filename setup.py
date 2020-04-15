#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "rb") as fh:
    long_description = fh.read()

setup(
    name="bone-pytex",
    version="0.1.1",
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
    install_requires=['pylatex'],
    scripts=[],
    # entry_points={
    #     'console_scripts': [
    #         'test = test.help:main'
    #     ]
    # }
)
