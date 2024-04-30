from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mst_app/__init__.py
from mst_app import __version__ as version

setup(
	name="mst_app",
	version=version,
	description="ERPnext App",
	author="ARD",
	author_email="aseel.gharbia@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
