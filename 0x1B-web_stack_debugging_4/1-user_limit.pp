# Change the OS configuration so that,
# it is possible to login with the holberton user open a file.
exec { 'update_soft_limit':
  command => 'sed -i "/holberton soft/s/4/4096/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'update_hard_limit':
  command => 'sed -i "/holberton hard/s/5/4096/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

