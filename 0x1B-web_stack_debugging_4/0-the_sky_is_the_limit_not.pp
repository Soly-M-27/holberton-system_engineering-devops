# Fix the stack so that server can process every and all requests
# within the traffic

exec {'modify max open files limit setting':
command => 'sed -i "s/15/10000" /etc/default/nginx && sudo srvice nginx restart',
path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
