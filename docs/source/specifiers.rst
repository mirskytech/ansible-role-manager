Specifiers
=============================


1. Install ``SomeRole`` by ``SomeOwner`` and its dependencies from `Ansible Galaxy <https://galaxy.ansible.com/>`_

  ::

	SomeOwner.SomeRole            # latest version
  	SomeOwner.SomeRole==1.0.4     # specific version
	SomeOwner.SomeRole,v1.0.4     # `ansible-galaxy` compatiblity
	SomeOwner.SomeRole>=1.0.4     # minimum version

For example: ``arm install SomeOwner.SomeRole,v1.0.4``

2. Install ``SomeRole`` by ``SomeOwner`` from a git repository

currently supported forms for cloning are ``git``, ``git+https`` and ``git+ssh``::

	>> git://git.myproject.org/SomeOwner/SomeRole
	>> git+https://git.myproject.org/SomeOwner/SomeRole
	>> git+ssh://git@git.myproject.org/SomeOwner/SomeRole
	>> git+git@git.myproject.org:SomeOwner/SomeRole
  
see :ref:`tagbranchcommit` and :ref:`alias` for additional options

3. Install ``SomeRole`` by ``SomeOwner`` from a mercurial (hg) repository

currently supported forms for cloning are ``hg+http``, ``hg+https``, ``hg+static-http`` and ``hg+ssh``::

	>> arm install hg+http://hg.myproject.org/MyProject
	>> arm install hg+https://hg.myproject.org/MyProject
	>> arm install hg+ssh://hg.myproject.org/MyProject

see :ref:`tagbranchcommit` and :ref:`alias` for additional options


4. Install ``SomeRole`` by ``SomeOwner`` from a subversion (svn) repository

*coming soon*

4. Install ``SomeRole`` by ``SomeOwner`` from a subversion (svn) repository

.. tagbranchcommit

Tag, Branch or Commit (git and hg only)
-------------------------------------------

Git and Mercurial use the same syntax for specifying a tag, branch or commit by using `@` plus the tag, branch or commit identifier.

  ::
      
	>> arm install git+git://git.myproject.org/MyProject.git@master
	>> arm install git+git://git.myproject.org/MyProject.git@v1.0
	>> arm install git+git://git.myproject.org/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709

.. alias
  
Alias (all)
------------------------

To change the role's name for local reference. Works with all forms above::


	>> arm install SomeOwner.SomeRoleName#alias=SomeName
  
Dependencies File
---------------------------


Install a list of requirements specified in a file.

  ::

    >> arm install -r requirements.txt
  
  
