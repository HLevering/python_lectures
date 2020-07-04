# if your project grows, you'll have to split up and organize your project
# modules are the way to do this
# a file represents a module
# you can use other modules by importing them
import math
# python has a whole battery of modules which can be imported

# you can import your own modules

import a_module
# use definitions from other modules by module.name syntax

print(a_module.foobar)

# it is possible to import only certain definitions
from a_module import foobar

# you can only specify a name, which you use to refer to a definition or module
import a_module as a
from a_module import foobar as foo

# python a lookup scheme for modules
# it has a var called "PYTHONPATH". This is a list of directories. Every .py
# file which is in a directory in PYTHONPATH can be imported
# you can modify PYTHONPATH  by
#import sys
#sys.insert("a_path_to_a_dict")
# this would add a_path_to_a_dict to PYTHONPATH
# This is only shown for completeness and because there are lots of advices
# like the above one on the internet
# But, you should rarely ever need to modify PYTHONPATH directly

# If you run a script via 'python my_script.py' python will add the directory
# of 'my_script.py' to PYTHONPATH, hence every .py file in the same directory
# as "my_script.py' can be imported as a module.
# Additionaly, every folder in a directory on PYTHONPATH, which contains a
# __init__.py file is considered as a module and other files in this folder are
# submodules. This recursivle works with subfolders, which contain __init__.py
# files, too

# this is valid
import b_module

#this is valid to
from b_module import c_module

# A python package is a collection of modules, which is bundled.
# There are tons of 3rd party packages and it is easy to use them with package
# managers (most commonly "pip" and pypy package archiv)
# 
# To enable a 3rd party package e.g. numpy for your current python interpreter
# just type pip install numpy in your console
# afterwards you will be able to use
# import numpy in your .py files
# There are lots of powerfull python packages out there in the wild
# a small collection

# numpy -> fast numeric computations
# scipy -> utility collection for scientific computations
# sympy -> symbolic math
# bokeh ->plotting and interactive documents
# tensorflow ->neuronal networks
# sklearn -> machine learning
# fastapi -> restful services
# pygame -> 3d engine
# pyqt -> native desktop applications
# cython -> compile python to native c code
# pytest -> easy to use unit test framework

# before writing your own code, check pypy if there is a python package, which
# fits your needs, but be careful if you install unkown 3rd party packages


# managing dependencies
# your project may require a lot of 3rd party packages and these packages may
# require other packages and so on. pip will manage all dependencies and
# dependencies of dependencies ... . However, there will be the case that you
# have a project A which requires package B and a project C which requires
# packae D, but package B and D are not compatible.
#
# Virtual environments to the rescue
# if you used pip install a_package, then this package will be installed
# globally
# It is therefore to provide each project/app its own python environment. The
# technique to do this is called virtual environment
# You can create a new virtual python environment by typing 'python -m venv
# my_environment_name'. This will create a new environment in the folder
# environment. In this folder there is a subfolder bin which contains a file
# 'activate' (on windows it should be in the script folder) you can use the new
# environment by sourcing the file. Type 'source
# my_environment_name/bin/activate'. Now you are using your new python
# environment. If you do a pip install numpy. Numpy is only installed locally
# into your environment and your global system interpreter is not polluted. As
# you sourced the activate file, a new command was made available in your
# console. "Deactivate". if you type 'deactivate' you will be using your global
# system python again. And if you 'source your_environment/bin/activate' you'll
# be using your local python again


# We rushed through the basics of python. In the next lessons we'll get a
# deeper look in the more advances capabilities of python and good programming
# practices in general
