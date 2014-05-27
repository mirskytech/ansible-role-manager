init
======================================

Creates the recommended directory structure to keep Ansible playbooks organized. And
provides examples to help get started.

**Usage**
++++++++++++++++++

  ::

    arm init [-h] (-p PLAYBOOK | -r ROLE | -m MODULE)
    
    optional arguments:
      -h, --help                            show this help message and exit                            
      -p PLAYBOOK, --playbook PLAYBOOK      create the recommended structure for a playbook                            
      -r ROLE, --role ROLE                  within a playbook, create directly & file structure for role                            
      -m MODULE, --module MODULE            within a playbook, create the structure for a custom module

Playbook
------------------

  ::

    <PLAYBOOK>/
        .gitignore
        production		        # inventory file for <named>

        site.yml		    	        # master playbook 
        webservers.yml			# playbooks for different tiers
        databases.yml
    
        roles/				# role playbooks
        library_roles/			# installed role playbooks
    
        group_vars/
            production1			# variables for groups within <named> inventory file
            production2
        host_vars/
            production1a.example.com	# variables associated with specific <host>
            production2b.example.com


Roles
--------------------		

  ::

    roles/<ROLE>/
        meta/
            main.yml	        	# role dependencies & properties
        files/
            bar.txt		        # files for use with the copy resource
            foo.sh		        # script files for use with the script resource
        handlers/
            main.yml		        # handlers file
        tasks/
            main.yml		        # primary task file
        templates/						
            example.cfg.j2		# files for use with the template resource
        vars/
            main.yml			# variables associated with this role

Module
---------------------

    ::

      library/<MODULE>/
          firstmodulecommand      # python scripts without ``.py``
          secondmodulecommand


Reference
+++++++++++++++++++

- `Ansible Directory Layout`_

.. _Ansible Directory Layout: http://docs.ansible.com/playbooks_best_practices.html#directory-layout
