

Requirement Specifiers
=============================


1. Install `SomeRole` by `SomeOwner` and its dependencies from `Ansible Galaxy`_

  ::

	SomeOwner.SomeRole            # latest version
  	SomeOwner.SomeRole==1.0.4     # specific version
	SomeOwner.SomeRole,v1.0.4     # `ansible-galaxy` compatiblity
	SomeOwner.SomeRole>=1.0.4     # minimum version

For example: `arm install SomeOwner.SomeRole,v1.0.4`

2. Install `SomeRole` by `SomeOwner` from a git repository.

Using pip-like specifiers

  ::

  >> git://git.myproject.org/SomeOwner/SomeRole
  >> git+https://git.myproject.org/SomeOwner/SomeRole
  >> git+ssh://git@git.myproject.org/SomeOwner/SomeRole
  >> git+git@git.myproject.org:SomeOwner/SomeRole

Or using git-like specifiers

  ::

  >> arm install git@git.myproject.org:SomeOwner/SomeRole.git

*Note*: any of the above specifiers can select a tag, branch or commit by using `@` plus the tag, branch or commit identifier.



3. Install `SomePackage` by `SomeOwner` from a mecurial repository.

  ::

  **coming soon**


3. Install a list of requirements specified in a file.  See the :ref:`Requirements files <Requirements Files>`.

  ::

  >> pip install -r requirements.txt
  
  
4. Install role from version control.

**git**

  ``arm`` will install the role with an alias of ``myproject``::
  
  >> arm install git+git://git.myproject.org/MyProject
  >> arm install git+https://git.myproject.org/MyProject  
  >> arm install git+ssh://git.myproject.org/MyProject
  
  
  specify a branch, tag or commit hash to install a specific version::
    
  >> arm install git+git://git.myproject.org/MyProject.git@master
  >> arm install git+git://git.myproject.org/MyProject.git@v1.0
  >> arm install git+git://git.myproject.org/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709
  
  * note: ``#egg=SomeName`` can be used with all git patterns above  
  
  **for example with github.com**
  
  >> arm install git+
  
  ( these will install )
  





4) Install a local project in "editable" mode. See the section on :ref:`Editable Installs <editable-installs>`.

  ::

  $ pip install -e .                     # project in current directory
  $ pip install -e path/to/project       # project in another directory


5) Install a project from VCS in "editable" mode. See the sections on :ref:`VCS Support <VCS Support>` and :ref:`Editable Installs <editable-installs>`.

  ::

  $ pip install -e git+https://git.repo/some_pkg.git#egg=SomePackage          # from git
  $ pip install -e hg+https://hg.repo/some_pkg.git#egg=SomePackage            # from mercurial
  $ pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomePackage         # from svn
  $ pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomePackage  # from 'feature' branch
  $ pip install -e git+https://git.repo/some_repo.git@egg=subdir&subdirectory=subdir_path # install a python package from a repo subdirectory


