

Requirement Specifiers
=============================


1. Install `SomeRole` by `SomeOwner` and its dependencies from `Ansible Galaxy`_

  ::

  >> arm install SomeOwner.SomeRole            # latest version
  >> arm install SomeOwner.SomeRole==1.0.4     # specific version
  >> arm install SomeOwner.SomeRole,v1.0.4     # `ansible-galaxy` compatiblity
  >> arm install SomeOwner.SomeRole>=1.0.4     # minimum version

2. Install `SomePackage` by `SomeOwner` with an alias

  ::

  >> arm install SomeOwner.SomeRoleName#egg=SomeName
  
  ( works with all formats listed above in #1 )

3) Upgrade an already installed `SomePackage` to the latest from PyPI.

  ::

  >> pip install --upgrade owner.role_name



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


