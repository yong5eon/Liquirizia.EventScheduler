# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

PKG = 'Liquirizia.EventScheduler'
SRC = 'src'
EXCLUDES = []
DESC = 'Event Scheduler of Python Modernized Application Framework Liquirizia'
WHO = 'Heo Yongseon'

PKGS = [PKG]
DIRS = {PKG: SRC}
for package in find_packages(SRC, exclude=EXCLUDES):
	PKGS.append('{}.{}'.format(PKG, package))
	DIRS['{}.{}'.format(PKG, package)] = '{}/{}'.format(SRC, package.replace('.', '/'))

setup(
	name=PKG,
	description=DESC,
	long_description=open('README.md', encoding='utf-8').read(),
	long_description_content_type='text/markdown',
	author=WHO,
	version=open('VERSION', encoding='utf-8').read(),
	packages=PKGS,
	package_dir=DIRS,
	include_package_data=False,
	classifiers=[
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
		'Application Framework :: Liquirizia',
		'Application Framework :: Liquirizia :: EventScheduler',
	],
	install_requires=[
		'Liquirizia@git+https://github.com/yong5eon/Liquirizia.git',
		'Liquirizia.EventRunner@git+https://github.com/yong5eon/Liquirizia.EventRunner.git',
		'apscheduler>=3.9.1'
	],
	python_requires='>=3.8'
)
