Infrastructure
==============

I'm not going to mess with containers for now.

Ansible will be my configuration managment tool of choice.

Development
-----------

The environment should work on a Vagrant setup
that launches at least a couple of VMs.

One VM should be a database VM. That's it. PostreSQL.

Another VM should have the app server.

My prototype did a decent job
of getting supervisord, nginx, and uwsgi linked together.
I don't know how that will need to evolve
with the hard separation between backend and frontend.

Production
----------

AWS EC2 and RDS at minimum. I'm not even close to thinking about that more.
