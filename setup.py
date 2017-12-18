#!/usr/bin/env python
# -*- conding:utf-8 -*-
__Author__ = "Yasin Li"
import  os
from setuptools import  setup

with open(os.path.join(os.path.dirname(__file__),'README.rst')) as readme:
     README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))
setup(
    name='django_1',
    version='0.1',
    packages=['django_app'],
    include_package_data=True,
    license='BSD License',
    description='A simple Djangi app to conduect Web-based django_app.',
    long_description=README,
    url='http://www.example.com',
    author='Yasin li',
    author_email='332841772@qq.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

