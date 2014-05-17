
Project page and docs:
    http://mirskytech.github.io/ansible-role-manager
Development:
    https://github.com/mirskytech/ansible-role-manager
Feature & issue tracking:
    https://github.com/mirskytech/ansible-role-manager/issues


Description
======================

Provides the following utilities:

- `init` Creates the Ansible recommended folder structure and initial core files for playbooks, roles and modules.

- `install` Installs Ansible roles from Ansible Galaxy or located in any version control repository (git, mercurial and svn).

- `uninstall` Remove dependencies from the playbook's library

- `freeze` Create list of installed dependencies for a playbook

see `arm help` for all availble commands.

Installation of ARM (Ansible Role Manager)
================================================

Standard installation::
  
    >> pip install arm
    
Installation for development::

    >> pip install -e git+https://github.com/mirskytech/ansible-role-manager.git#egg=role-manager
    
Manual installation::

    >> git clone https://github.com/mirskytech/ansible-role-manager.git
    >> python setup.py install
  
  
Dependencies
======================

- ansible
- requests
- gitpython (0.3.2.RC1)
- colorama


References
==================

-  Ansible http://docs.ansible.com/

-  Ansible Galaxy https://galaxy.ansible.com/explore



Release Notes & Roadmap
===========================

TBD



