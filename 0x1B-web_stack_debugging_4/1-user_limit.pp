exec { 'update_limits':
  command => 'echo -e "holberton\t\tsoft\tfile\t\t4096\n" >> /etc/security/limits.conf',
  path    => '/bin'
}
