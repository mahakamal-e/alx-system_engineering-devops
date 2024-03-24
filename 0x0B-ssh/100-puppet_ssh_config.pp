# ensure configration file exists

file {'/etc/ssh/ssh_config':
    ensure  => present,
    content => 'Host *
    PasswordAuthentication no
    IdentityFile ~/.ssh/school',
}
