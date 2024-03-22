class { 'python3': }  # Include python3 class for python3 support

package { 'Flask':
  # Ensure Flask is installed
  ensure => present,
  # Use pip3 provider to install from the Python Package Index (PyPI)
  provider => 'pip3',
  # Specify the required version
  require => Class['python3'],  # Make sure python3 is installed first
  # Specify exact version of Flask
  ensure_version => '2.1.0',
}
