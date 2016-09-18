#!/usr/bin/env python

#@author Rajmani Arya

from setuptools import setup

the_version = open("VERSION").read().strip()
print "Packaging the version " + the_version

setup(
        name="lcmd",
        version=the_version,
        description="Powerful linux commands simplified",
        url="https://github.com/rajmani1995/LCmd.git",
        author="Rajmani Arya",
        author_email="rajmani1995@gmail.com",
        license='MIT',
        packages=["lcmd"],
        entry_points="""
             [console_scripts]
             open = lcmd.open:main
             search = lcmd.search:main
             code = lcmd.code:main
             math = lcmd.math:main
        """,
        install_requires=[
            'argparse',
        ],
        zip_safe=False
)
