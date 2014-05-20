Release Notes
-------------------

0.4
==================

release: TBD

- commands and routes are now found by looking for subclasses of arm.commands.Command and arm.routes.Route, respectively
- common dictionary of regular expressions for routes
- routes now need to define their name (__unicode__)



0.3.1
=================

released: 2014-05-19

- updated comments & documentation


0.3
=================

released: 2014-05-18

-  create ``freeze`` command to capture dependencies
-  ``uninstall`` to remove role
-  add ``alias`` when linking ``/library\_roles``  into ``/roles``
-  fetch/install roles from ``requirements.txt`` file


0.2
============

released: 2014-05-08

-  create fetch role from any git server
-  create ``help`` command (alias to -h)
-  fetch dependencies

0.1
=============

released: 2014-04-29

-  framework for creating commands & fetching rolls
-  created ``init`` command for playbook and module template
-  create ``install`` command & fetching from ansible galaxy (no
   dependencies)

Feature Requests
================

-  make library\_roles read-only and provide a ``-e`` mechanism
-  add `upload` command to add role into galaxy
-  mercurial support (v 0.4) **
-  svn support (v 0.4) **
-  fetch roles from within other playbooks or "library" of roles

** note : ansible galaxy meta format only supports git on github.com (specifically ``github_owner`` and ``github_repo``)
