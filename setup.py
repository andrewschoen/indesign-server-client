# -*- coding: utf-8 -*-


from setuptools import find_packages
from setuptools import setup


setup(
    name='indesign-server-client',
    version='0.0.1',
    description='Provides a simple wrapper for the InDesign Server SOAP service.',
    license='MIT',
    url='https://github.com/andrewschoen/indesign-server-client',
    packages=find_packages(),
    install_requires=['suds>=0.4'],
    author='Andrew Schoen',
    author_email='andrew.schoen@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)