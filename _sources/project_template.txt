

init
======================================

Creates the recommended directory structure to keep Ansible playbooks organized. And
provides boilerplate with examples to help get started.

From http://ansible.com/blahblahblah

New Projects
------------------

-p, --project::

    project/
		.gitignore
        inventory
		playbook.yml
		roles/
		common/
		group_vars/
		host_vars/

Roles
--------------------		
		
-r, --role::
		roles/role/
			meta/
			meta/main.yml
			files/
			handlers/
			handlers/main.yml
			tasks/
			tasks/main.yml
			templates/
			templates/example.cfg.j2
			var/
			var/main.yml
