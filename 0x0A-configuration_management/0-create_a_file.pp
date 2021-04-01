# Create file /tmp/holberton if not exists, set perms, owner, group, and content
file { '/tmp/holberton':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}