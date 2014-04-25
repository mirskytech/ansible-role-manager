init
======================================

Creates the recommended directory structure to keep Ansible playbooks organized. And
provides boilerplate with examples to help get started.

From http://ansible.com/blahblahblah

New Projects
------------------

-p, --playbook::

    playbook/
		.gitignore
		production				# inventory file for <named>

		site.yml				# master playbook 
		webservers.yml			# playbooks for different tiers
		databases.yml

		roles/					# role playbooks
		library_roles/			# installed role playbooks

		group_vars/
				production1		# variables for groups within <named> inventory file
				production2
		host_vars/
				production1a.example.com		# variables associated with specific <host>
				production2b.example.com
		

Roles
--------------------		
		
-r, --role::
	roles/role/
		meta/
				main.yml				# role dependencies & properties
		files/
				bar.txt					# files for use with the copy resource
				foo.sh					# script files for use with the script resource
		handlers/
				main.yml				# handlers file
		tasks/
				main.yml				# primary task file
		templates/						
				example.cfg.j2			# files for use with the template resource
		vars/
				main.yml				# variables associated with this role

Module
---------------------

-m, --module::


__in progress__
	