

*0.0.5*

expected: 2014-05-23

-  fetch roles from within other repositories
-  svn support

*0.0.4*

expected: 2014-05-18

-  fetch/install roles from ``requirements.txt`` file
-  mercurial support

*0.0.3*

expected: 2014-05-16

-  create ``freeze`` command to capture dependencies
-  ``remove`` (or ``uninstall``?) to remove role
-  add ``alias`` when linking library\_roles -> roles

*release 0.0.2*

released: 2014-05-08

-  create fetch role from any git server
-  create ``help`` command (alias to -h)
-  fetch dependencies

*release 0.0.1*

released: 2014-04-29

-  framework for creating commands & fetching rolls
-  created ``init`` command for playbook and module template
-  create ``install`` command & fetching from ansible galaxy (no
   dependencies)

Future
------

-  make library\_roles read-only and provide a ``-e`` mechanism
-  warn when upgrading a role that has been modified
