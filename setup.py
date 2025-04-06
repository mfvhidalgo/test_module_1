from setuptools import setup, find_packages

setup(
    name='func1_suite',
    version='0.1',
    py_modules=[],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    url='https://github.com/mfvhidalgo/test_module_1',
    author='',
    author_email='',
    description='',
    test_suite='tests',
)
