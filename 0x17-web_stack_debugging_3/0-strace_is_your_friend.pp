# replacing the string "phpp" with "php" 
exec { 'replace phpp to php':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/'
}
