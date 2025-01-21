from setuptools import find_packages, setup

setup(
    name='regdurations',
    packages=find_packages(include=['regdurations']),
    version='1.0.2',
    python_requires='>=3.9',
    extras_require={
        'find_relativedelta': ['dateutil']
    },
    description='Parse user-provided duration strings using regular expressions',
    author='CrisMystik'
)
