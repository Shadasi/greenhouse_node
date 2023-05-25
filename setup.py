# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='greenhouse_node',
    version='0.1.0',
    description='Script for running on raspberry pi to collect data from DHT20 - AHT20 temperature and humidity sensor',
    long_description=readme,
    author='Stephen Albrecht',
    author_email='Shadasi@users.noreply.github.com',
    url='https://github.com/Shadasi/greenhouse_node',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)