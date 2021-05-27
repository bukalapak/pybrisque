# coding=utf-8
"""Setup file for distutils / pypi."""
try:
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    pass

from setuptools import setup, find_packages


setup(
    name='pybrisque',
    version='1.0',
    packages=find_packages(),
    package_data={
        'brisque': ['allmodel']
    },
    license='GPL',
    author='Akbar Gumbira',
    author_email='akbar.gumbira@bukalapak.com',
    url='https://github.com/bukalapak/pybrisque',
    description=('A package for BRISQUE metric calculation.'),
    long_description=open('README.md').read(),
    install_requires=[
        'numpy',
        'scipy',
        'opencv-python',
        'libsvm'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

    ]
)
