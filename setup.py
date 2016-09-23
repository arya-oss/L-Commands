#!/usr/bin/env python

#@author Rajmani Arya

from distutils.core import setup

setup(
        name="lcmd",
        version="0.0.1",
        description="Powerful linux commands simplified",
        url="https://github.com/rajmani1995/L-Commands.git",
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
