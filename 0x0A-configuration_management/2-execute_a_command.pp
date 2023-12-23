# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill': 
   command => 'pkill -k killmenow',
   path    => ['/usr/bin', '/usr/sbin']
}
