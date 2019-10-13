import setuptools
import re
import os


# Fields marked as "Optional" may be commented out.
setuptools.setup(
    name="parking_lot",  # Required
    version=1.0,  # Required
    author="anji",  # Optional
    description="parking_lot",  # Required
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    include_package_data=True  # Optional
    )