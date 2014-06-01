Specifiers
=============================

Refer to :ref:`alias` for more information on local naming of installed roles.

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
  
3. Install ``SomeRole`` by ``SomeOwner`` from a mercurial (hg) repository

currently supported forms for cloning are ``hg+http``, ``hg+https``, ``hg+static-http`` and ``hg+ssh``::

	>> arm install hg+http://hg.myproject.org/SomeRole
	>> arm install hg+https://hg.myproject.org/SomeRole
	>> arm install hg+ssh://hg.myproject.org/SomeRole
	
specify a revision number, a revision hash, a tag name or a local branch name using ``@``::

    >> arm install hg+http://hg.myproject.org/SomeRole@da39a3ee5e6b
    >> arm install hg+http://hg.myproject.org/SomeRole@2019
    >> arm install hg+http://hg.myproject.org/SomeRole@v1.0
    >> arm install hg+http://hg.myproject.org/SomeRole@special_feature

4. Install ``SomeRole`` by ``SomeOwner`` from a subversion (svn) repository

currently supported forms for checkout are ``svn``, ``svn+svn``, ``svn+http``, ``svn+https``, ``svn+ssh``.

    >> arm install svn+svn://svn.myproject.org/svn/SomeRole
    >> arm install svn+http://svn.myproject.org/svn/SomeRole/trunk
	
You can also give specific revisions to an SVN URL, like so::

	>> arm install svn+svn://svn.myproject.org/svn/SomeRole/branch/mybranch@{20080101}
	>> arm install svn+http://svn.myproject.org/svn/SomeRole/trunk@2019
	
which checks out revison from 2008-01-01 or revision 2019, spectively
	
5. Install ``SomeRole`` by ``SomeOwner`` from a bazaar (bzr) repository

currently supported forms for checkout are ``bzr+http``, ``bzr+https``, ``bzr+ssh``,
``bzr+sftp``, ``bzr+ftp`` and ``bzr+lp``::

    >> arm install bzr+http://bzr.myproject.org/SomeRole/trunk
    >> arm install bzr+sftp://user@myproject.org/SomeRole/trunk
    >> arm install bzr+ssh://user@myproject.org/SomeRole/trunk
    >> arm install bzr+ftp://user@myproject.org/SomeRole/trunk
    >> arm install bzr+lp:SomeRole
	
tags or revisions can be installed using ``@``::

    >> arm install bzr+https://bzr.myproject.org/SomeRole/trunk@2019 
    >> arm install bzr+http://bzr.myproject.org/SomeRole/trunk@v1.0

.. _alias:
  
Alias
------------------------

To change the role's name for local reference. Works with all forms above::


	>> arm install SomeOwner.SomeRoleName#alias=SomeName
  
Dependencies File
---------------------------


Install a list of requirements specified in a file.

  ::

    >> arm install -r requirements.txt
  
  
