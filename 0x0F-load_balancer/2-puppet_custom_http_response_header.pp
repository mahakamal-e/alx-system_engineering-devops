# Update the system
exec { 'apt update':
  command => 'apt-get update',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
}

# Install Nginx
package { 'nginx':
  ensure => installed,
  require => Exec['apt update'],
}

# Allow Nginx through the firewall
exec { 'Nginx HTTP':
  command => 'ufw allow "Nginx HTTP"',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  require => Package['nginx'],
}

# Set the custom HTTP response header
file { '/etc/nginx/conf.d/custom-header.conf':
  ensure  => file,
  content => 'server_tokens off;
              add_header X-Served-By $hostname;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Package['nginx'], File['/etc/nginx/conf.d/custom-header.conf']],
}
