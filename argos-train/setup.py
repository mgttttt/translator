from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()

setup(
    name='argostrain',
    version='0.1',
    description='Training scripts for Argos Translate',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Argos Open Technologies, LLC',
    author_email='admin@argosopentech.com',
    url='https://www.argosopentech.com',
    packages=find_packages(),
    install_requires=required_packages,
    python_requires=">=3.8",
    include_package_data=True,
    scripts=['bin/argos-train', 'bin/argos-train-init'],
)
