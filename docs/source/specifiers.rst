Requirement Specifiers
=============================


1. Install `SomeRole` by `SomeOwner` and its dependencies from `Ansible Galaxy`_

  ::

	SomeOwner.SomeRole            # latest version
  	SomeOwner.SomeRole==1.0.4     # specific version
	SomeOwner.SomeRole,v1.0.4     # `ansible-galaxy` compatiblity
	SomeOwner.SomeRole>=1.0.4     # minimum version

For example: `arm install SomeOwner.SomeRole,v1.0.4`

2. Install `SomeRole` by `SomeOwner` from a git repository

**using pip-like specifiers**

  ::

	>> git://git.myproject.org/SomeOwner/SomeRole
	>> git+https://git.myproject.org/SomeOwner/SomeRole
	>> git+ssh://git@git.myproject.org/SomeOwner/SomeRole
	>> git+git@git.myproject.org:SomeOwner/SomeRole

**using git-like specifiers**

  ::

	>> arm install git@github.com:Owner/MyProject.git
	>> arm install https://github.com/Owner/MyProject.git
	>> arm install ssh://git@github.com/Owner/MyProject.git
  
Any of the above can specify a tag, branch or commit by using `@` plus the tag, branch or commit identifier.

  ::
      
	>> arm install git+git://git.myproject.org/MyProject.git@master
	>> arm install git+git://git.myproject.org/MyProject.git@v1.0
	>> arm install git+git://git.myproject.org/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709


3. Install `SomeRole` by `SomeOwner` from a mercurial (hg) repository

*coming soon*

4. Install `SomeRole` by `SomeOwner` from a subversion (svn) repository

*coming soon*

  
Alias
------------------------

To change the role's name for local reference

  ::

	>> arm install SomeOwner.SomeRoleName#alias=SomeName
  
Dependencies File
---------------------------


Install a list of requirements specified in a file.  See the :ref:`Requirements files <Requirements Files>`.

  ::

    >> arm install -r requirements.txt
  
  
