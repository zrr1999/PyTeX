from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pytex",
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
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
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
