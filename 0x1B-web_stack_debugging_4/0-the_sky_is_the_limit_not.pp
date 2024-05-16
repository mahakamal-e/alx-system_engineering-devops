#Change the limit amount of traffic in the Nginx configuration file.
exec { 'set limit':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}

exec { 'nginx restart service':
  command => 'service nginx restart',
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
}
