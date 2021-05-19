# Execute command to fix typo in wp-settings
exec { 'sed':
  command => 'sed -i 's/phpp/php/' /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}