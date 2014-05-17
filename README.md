python-primogen
===============

[![Build Status](https://travis-ci.org/steenzout/python-primogen.svg?branch=master)](https://travis-ci.org/steenzout/python-primogen)
[![Code Health](https://landscape.io/github/steenzout/python-primogen/master/landscape.png)](https://landscape.io/github/steenzout/python-primogen/master)
[![Coverage Status](https://coveralls.io/repos/steenzout/python-primogen/badge.png)](https://coveralls.io/r/steenzout/python-primogen)
[![Requirements Status](https://requires.io/github/steenzout/python-primogen/requirements.png?branch=master)](https://requires.io/github/steenzout/python-primogen/requirements/?branch=master)

This repository's goal is to be a starting point for Python projects.

It uses:

- [git](http://git-scm.com) for version control
- [pip](http://www.pip-installer.org/en/latest/) to manage Python packages
- [tox](http://tox.readthedocs.org/en/latest/) for automation and setup development environments
- [Sphinx](http://sphinx-doc.org) for documentation


company
-------

This is the directory which will hold your files.

Rename "company" with your company's name or product.

In this empty project the company package is a namespace package,
meaning it was defined in another repository.

You may not need to do this but it's here to make an example of how to define namespace packages,
what to add on the __init__.py file and in the setup.py file.


docs
----

Directory where you'll store the [Sphinx](http://sphinx-doc.org) configuration files and
where the documentation will be generated.


.gitignore
----------

File where you specify which files [Git](http://en.wikipedia.org/wiki/Git_(software)) should ignore.

A generic file has been provided.

You can use [gitignore.io](http://www.gitignore.io) to
produce other files that will better suit your development environment.

For more information, you can check "[git-scm.com : gitignore](http://git-scm.com/docs/gitignore)".


LICENSE
-------

The Apache 2 license.

Feel free to replace for another license that will be more suitable to the purpose of your project.


pytest.ini
----------

The [pytest](https://pytest.org/latest/index.html) configuration file.

You can read
"[pytest : Changing standard (Python) test discovery](https://pytest.org/latest/example/pythoncollection.html)"
for more information on how to use this file to customize [pytest](https://pytest.org/latest/index.html)'s behavior.


README.md
---------

This file.

Check "[here](http://daringfireball.net/projects/markdown/syntax)" for help
with [Markdown](http://daringfireball.net/projects/markdown/) syntax.


requirements.txt
----------------

On this file you specify the list of packages the project depends.

Read "[pip : Requirement Files](http://www.pip-installer.org/en/latest/user_guide.html#requirements-files)"
to understand how you can properly use this file to define your project's dependencies.


setup.py
--------

The setup script whre you'll describe the project / product, authors, maintainers and
information on how to distribute it.

Read "[Python : 2. Writing the Setup Script](http://docs.python.org/2/distutils/setupscript.html)",
for more information.


tests
-----

The directory where you should add your unit tests.


test-requirements.txt
---------------------

On this file you specify the list of packages the project needs to run its tests.

An example of the possible contents of this file has been provided.

Read "[pip : Requirement Files](http://www.pip-installer.org/en/latest/user_guide.html#requirements-files)"
to understand how you can properly use this file to define your project's test dependencies.


tox.ini
-------

The [tox](http://tox.readthedocs.org/en/latest/) configuration file.

It contains basic information about your project and test environments.

I recommend [installling tox](http://tox.readthedocs.org/en/latest/install.html) and
use it to run your tests and generate the documentation.

```
# run the tests
$ tox

# generate the documentation
$ tox -e docs
```
