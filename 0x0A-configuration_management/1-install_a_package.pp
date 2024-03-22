#!/usr/bin/pup
# Install flask from pip3
package{'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}

notify { 'Flask installed successfully':
  message => 'Flask version 2.1.0 installed successfully',
}
