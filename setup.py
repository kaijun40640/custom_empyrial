from setuptools import setup

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='empyrial',
    version='1.9.9',
    description='An Open Source Portfolio Management Framework for Everyone 投资组合管理',
    py_modules=['empyrial'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kaijun40640/Empyrial/',
    author="Kai Jun",
    author_email="kaijun40640@gmail.com",
    license='MIT',
    install_requires=[
        'numpy',
        'matplotlib',
        'datetime',
        'empyrical',
        'quantstats',
        'yfinance',
        'ipython',
        'fpdf',
        'pyportfolioopt'

    ],
)
