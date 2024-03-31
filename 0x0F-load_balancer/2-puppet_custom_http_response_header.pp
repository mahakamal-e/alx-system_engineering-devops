# Creating a custom HTTP header response with Puppet.

exec { 'update':
  command => 'apt-get update',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
}

package { 'nginx':
  ensure => installed,
  require => Exec['update'],
}

exec { 'Nginx HTTP':
  command => 'ufw allow "Nginx HTTP"',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  require => Package['nginx'],
}

file { '/etc/nginx/conf.d/custom-header.conf':
  ensure  => file,
  content => 'server_tokens off;
              add_header X-Served-By $hostname;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Package['nginx'], File['/etc/nginx/conf.d/custom-header.conf']],
}
