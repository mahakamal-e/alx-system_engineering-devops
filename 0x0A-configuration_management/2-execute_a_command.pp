# Task using Puppet, kill prosses using exec

exec{'run a command':
        command => 'pkill killmenow',
        path    => ['/usr/bin','/usr/sbin','/bin'],
}
