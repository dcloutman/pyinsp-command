#!/usr/bin/env python3
"""Setup script for pyinsp package."""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

setup(
    name='pyinsp',
    version='0.0.1',
    description='A Python syntax inspector similar to PHP\'s php -l command',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='David Cloutman',
    url='https://github.com/dcloutman/pyinsp-command',
    packages=find_packages(),
    py_modules=[],
    package_dir={"": "."},
    install_requires=[
        'click>=8.2.1,<9.0.0',
    ],
    entry_points={
        'console_scripts': [
            'pyinsp=bin.pyinsp:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
    python_requires='>=3.7',
    license='MIT',
    keywords='python linter syntax checker php-l',
)
