# Fix typo in wp-settings file
exec { 'fix':
  environment => ['DIR=/var/www/html/wp-settings.php',
                  'OLD=phpp',
                  'NEW=php'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}