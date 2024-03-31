# 2-puppet_custom_http_response_header.pp
file { '/etc/facter/facts.d/custom_hostname.txt':
  ensure  => file,
  content => "hostname=${hostname}",
}

# Update package lists
exec { 'update':
  command  => 'apt-get update',
  provider => shell,
}

# Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Manage custom HTTP header in Nginx configuration
file_line { 'custom_http_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => '    add_header X-Served-By $hostname;',
  match   => '^\s*location / {$',
  require => File['/etc/nginx/sites-available/default'],
}

# Manage Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
