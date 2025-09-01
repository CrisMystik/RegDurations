from setuptools import find_packages, setup

setup(
    packages=find_packages(include=['regdurations']),
    package_data={
        'regdurations': ['py.typed']
    }
)
