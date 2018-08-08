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
    version='0.9.3',
    packages=find_packages(),
    py_modules=['brisque', 'utilities'],
    package_data={
        '': ['allmodel', 'LICENSE']
    },
    include_package_data=True,
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
    dependency_links=[
        'git+https://github.com/akbargumbira/libsvm-python.git@master#egg=libsvm-0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ]
)
