# File: execute_a_command.pp

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin', # Specify the path to the pkill command
  refreshonly => true,
}