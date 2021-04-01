# Execute command pkill to kill a process.
exec { 'pkill':
  command => 'pkill -x killmenow',
  path    => '/usr/bin',
}