# puppet script that updates the ulimit to address high amount of failed requests.
exec { 'nginx-ulimit-fix' :
  command => "bash -c \"sed -iE 's/^ULIMIT=.*/ULIMIT=\\\"-n 8192\\\"/' \
/etc/default/nginx; service nginx restart\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}
