from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in praveen_library_management/__init__.py
from praveen_library_management import __version__ as version

setup(
	name="praveen_library_management",
	version=version,
	description="Library Management",
	author="nxweb",
	author_email="info@nxweb.co.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
