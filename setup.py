from setuptools import setup, find_packages

setup(
    name="pytex",
    version="0.1.0",
    keywords=("LaTex", "MarkDown"),
    description="一个用来简化LaTex编写的python库",
    long_description="一个用来简化LaTex编写的python库",
    license="GPL-3.0 Licence",
    url="",
    author="zrr",
    author_email="2742392377@qq.com",
    packages=find_packages(),
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
