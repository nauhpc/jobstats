#!/usr/bin/env python


import os
import sys
import setuptools


with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name='jobstats',
    version='1.2.5',
    author='Chance Nelson',
    author_email='chance-nelson@nau.edu',
    description='view Slurm job resource efficiencies',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nauhpc/jobstats",
    include_package_data=True,
    packages=setuptools.find_packages(),
    scripts=['jobstats/jobstats', 'jobstats/group_efficiency'],
    data_files=[('config', ['jobstats/jobstats-config.ini'])],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
    ],
)
