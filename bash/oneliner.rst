Execute remote shell command in multiple hosts
----------------------------------------------

Everything after ``--`` is executed in each remote host within a temporary  fab
``run`` call:: 

    fab -H host1,host2 -- "sudo apt-get update && apt-get upgrade"

Show exit code when program terminates abnormally
-------------------------------------------------

This can be inserted into ``PS1`` environmental variable::

    ${?/#0/}
