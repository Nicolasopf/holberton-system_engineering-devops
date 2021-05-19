# Execute command to fix typo in wp-settings
exec { 'fix':
  command => 'sudo sed -i "s/phpp/php/" $DIR',
  path    => ['/usr/bin', '/bin'],
  returns => [0, 1],
}
