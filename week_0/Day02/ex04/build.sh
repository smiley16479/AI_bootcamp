#!/bin/bash

#https://www.freecodecamp.org/news/build-your-first-python-package/
python setup.py sdist bdist_wheel

pip install ./dist/Loadingmodule-0.0.1.tar.gz # doit etre change pour le bon nom