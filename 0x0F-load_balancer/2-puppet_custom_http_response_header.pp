# Creating a custom HTTP header response with Puppet.
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}
package { 'nginx':
  ensure => latest,
}

package { 'nginx':
  ensure => installed,
}

firewall { 'Allow Nginx HTTP':
  ensure  => 'present',
  dport   => 80,
  proto   => 'tcp',
  action  => 'accept',
}

file { '/etc/nginx/conf.d/custom-header.conf':
  ensure  => file,
  content => 'server_tokens off;
              add_header X-Served-By $hostname;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
