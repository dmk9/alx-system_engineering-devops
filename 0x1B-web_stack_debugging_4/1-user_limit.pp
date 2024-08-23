exec {'change-os-config-holberton-user':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 88888/' /etc/security/limits.conf; sed -i 's/holberton soft nofile 4/holberton soft nofile 88888/' /etc/security/limits.conf;",
  path    => '/usr/bin:/usr/sbin:/bin'
}
