# Execute command to fix typo in wp-settings
exec { 'sed':
  command => 'sed -i "s/phpp/php/" $DIR',
  path    => ['/usr/bin', '/bin'],
  returns => [0, 1],
}
