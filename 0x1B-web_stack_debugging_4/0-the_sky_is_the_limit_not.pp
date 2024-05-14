#Change the limit amount of traffic in the Nginx configuration file.
exec { 'change the limit':
    command => 'sudo sed -i 's/15/4096/g' /etc/default/nginx'  && sudo service nginx restart',
    path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}
