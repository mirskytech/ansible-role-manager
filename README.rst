
Project page and docs:
    http://mirskytech.github.io/ansible-role-manager
Development:
    https://github.com/mirskytech/ansible-role-manager
Feature & issue tracking:
    https://github.com/mirskytech/ansible-role-manager/issues
Package Index:
    https://pypi.python.org/pypi/ansible-role-manager

Description
======================

Provides the following utilities:

- ``init`` Creates the Ansible recommended folder structure and initial core files for playbooks, roles and modules.

- ``install`` Installs Ansible roles from Ansible Galaxy or located in any version control repository (git, mercurial and svn).

- ``uninstall`` Remove dependencies from the playbook's library

- ``freeze`` Create list of installed dependencies for a playbook

see ``arm help`` for all availble commands.

Installation of Ansible Role Manager (ARM)
================================================

Standard installation::
  
    >> pip install ansible-role-manager
    
or installation for development::

    >> pip install -e git+https://github.com/mirskytech/ansible-role-manager.git#egg=role-manager
    
or manual installation::

    >> git clone https://github.com/mirskytech/ansible-role-manager.git
    >> python setup.py install

Get Started
======================

Create a well-structured playbooks (directory structure, initial files)::

    >> arm init -p MyNewPlaybook
    
Install a role from Ansible Galaxy::

    >> arm install github_owner.github_repo
    
Install a role from an arbitrary git repository::

    >> arm install git+ssh://github.com/github_owner.github_repo.git
  
Dependencies
======================

- mercurial
- git

- python
    - ansible
    - requests
    - gitpython (0.3.2.RC1)
    - colorama
    - hgapi


References
==================

-  Ansible http://docs.ansible.com/

-  Ansible Galaxy https://galaxy.ansible.com/explore



Release Notes & Roadmap
===========================

http://mirskytech.github.io/ansible-role-manager/releasenotes.html


