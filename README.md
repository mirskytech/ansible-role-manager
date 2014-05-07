Ansible Role Manager
=======================

Manager to install, uninstall, update roles from Ansible Galaxy &amp; version control repositories.

**under development**

- [Project Home](http://mirskytech.github.io/ansible-role-manager/)

- [Github Home](https://github.com/mirskytech/ansible-role-manager)

- [Issue Tracking](https://github.com/mirskytech/ansible-role-manager/issues)


References
----------------------

- [Ansible](http://docs.ansible.com/)

- [Ansible Galaxy](https://galaxy.ansible.com/explore#/)

Release Notes & Schedule
----------------------

*0.0.4*
expected: 2014-05-14

- fetch/install roles from `requirements.txt` file
-
-

*0.0.3*
expected: 2014-05-10

- create `freeze` command to capture dependencies
- `remove` (or `uninstall`?) to remove role
- add `alias` when linking library_roles -> roles

*release 0.0.2*
expected: 2014-05-07

- create fetch role from git
- create `help` command (alias to -h)
- fetch dependencies (optional)


*release 0.0.1*
released: 2014-04-29

- framework for creating commands & fetching rolls
- created `init` command for playbook and module template
- create `install` command & fetching from ansible galaxy (no dependencies)