# Creating a custom HTTP header response with Puppet.

file { '/etc/facter/facts.d/custom_hostname.txt':
  ensure  => file,
  content => "hostname=${hostname}",
}

package { 'nginx':
  ensure  => present,
  require => Exec['update'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

file_line { 'header line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "	add_header X-Served-By ${::hostname};",
  match  => '^\tlocation / {',
  require => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}
