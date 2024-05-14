# Change the OS configuration so that,
# it is possible to login with the holberton user open a file.
exec { 'update_soft_limit':
  command => "sed -i '/^holberton\\s.*nofile/d; $ a\\holberton soft nofile 4096' /etc/security/limits.d/holberton.conf",
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  notify  => Exec['reload_pam'],
}

exec { 'update_hard_limit':
  command => "sed -i '/^holberton\\s.*nofile/d; $ a\\holberton hard nofile 8192' /etc/security/limits.d/holberton.conf",
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  notify  => Exec['reload_pam'],
}

exec { 'reload_pam':
  command     => 'pam-auth-update --force',
  refreshonly => true,
}
