# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill': 
   command  => 'pkill -f killmenow',
   provider => 'shell',
   path     => ['/usr/bin', '/usr/sbin'],
}
