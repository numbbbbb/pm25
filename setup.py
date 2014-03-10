#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup

setup(
    name="pm25",
    version="0.1.4",
    description="实时获取城市的详细pm2.5数据",
    author="numbbbbb",
    author_email="lj925184928@gmail.com",
    packages=["pm25", ],
    url="https://github.com/numbbbbb/pm25",
    license="WTFPL",
    install_requires=["beautifulsoup4>=4.3.2"],
    long_description=open("README.md").read(),
)
