from setuptools import setup, find_packages

requires = [
    'matplotlib',
    'numpy'
]

setup(
    name='py-raytrace',
    version='1.0',
    description='Python raytracer',
    author='Tim Wakeham',
    url='http://tjwakeham.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
