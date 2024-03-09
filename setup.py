from setuptools import setup, find_packages

setup(
    name='assignment1',
    version='1.0',
    author='Jagadeeswara Reddy Gummi Reddy',  
    author_email='gummireddy.j@ufl.edu',  
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
