.. AnsibleRoleManager documentation master file, created by
    sphinx-quickstart on Thu Jan 30 08:20:20 2014.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.

Ansible Role Manager
======================================

Manager to install, uninstall, update roles from Ansible Galaxy & git repositories.

Uses design patterns from `pip` [#]_ and `git` [#]_.

Inspiration from `ansible-galaxy` [#]_ and `librarian-ansible` [#]_.


Sections
----------------------------------

* :ref:`intro-docs`
* :ref:`command-docs`


.. _intro-docs:

Getting Started
---------------------

.. toctree::
    :maxdepth: 1

    installation
    


.. _command-docs:

Commands
------------------

.. toctree::
    :maxdepth: 1

    init
    install
    remove
    update
    freeze
    
Reference
------------------

.. toctree::
    :maxdepth: 1
    
    specifiers


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. rubric:: Footnotes

.. [#] http://www.pip-installer.org/en/latest/reference/pip_install.html#pip-install-examples
.. [#] http://git-scm.com/docs/git-init
.. [#] https://galaxy.ansible.com/intro
.. [#] https://github.com/bcoe/librarian-ansible

