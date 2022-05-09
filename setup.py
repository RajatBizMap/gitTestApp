from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gittest/__init__.py
from gittest import __version__ as version

setup(
	name="gittest",
	version=version,
	description="test",
	author="TEst@gmail.com",
	author_email="test@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
