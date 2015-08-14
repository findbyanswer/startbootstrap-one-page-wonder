from setuptools import setup, find_packages

INSTALL_REQUIRES = []

setup(
    name='findbyanswers_website',
    version='0.0.1',
    description='findbyanswers website',
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=INSTALL_REQUIRES,
)
