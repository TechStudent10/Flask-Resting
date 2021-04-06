"""
Flask-Resting
-------------

A simple REST-API module for Flask.
"""
from setuptools import setup


setup(
    name='Flask-Resting',
    version='1.0',
    url='https://github.com/TechStudent11/Flask-Resting',
    license='BSD',
    author='Damola Mohammed',
    author_email='mohammeddam1@outlook.com',
    description='A simple REST-API module for Flask.',
    long_description=__doc__,
    packages=['flask_resting'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)