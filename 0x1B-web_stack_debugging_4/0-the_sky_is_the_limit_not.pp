exec { 'nginx-ulimit-fix' :
  command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 8192\"/' /etc/default/nginx; service nginx restart",
  path    => '/usr/bin:/usr/sbin:/bin'

}
