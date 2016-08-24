#!/usr/bin/env python
from setuptools import setup

version = '0.8'

setup(
    name='yandex-maps',
    version=version,
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',
    url='https://bitbucket.org/kmike/yandex-maps/',

    description='Yandex.Maps API python wrapper with optional django integration.',
    long_description=open('README.rst').read() + open('CHANGES.rst').read(),
    license='MIT license',
    requires=['django (>=1.7)'],
    install_requires=['requests'],
    packages=['yandex_maps', 'yandex_maps.templatetags', 'yandex_maps.migrations'],
    package_data={'yandex_maps': ['templates/yandex_maps/*']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
