# Installs Nginx and adds a custom HTTP header

exec { 'update':
  command => 'sudo apt-get -y update',
  path    => ['/usr/bin', '/bin'],
  before  => Exec['install_nginx'],
}

exec { 'install_nginx':
  command => 'sudo apt-get -y install nginx',
  path    => ['/usr/bin', '/bin'],
  notify  => Exec['configure_custom_header'],
}

exec { 'configure_custom_header':
  command     => 'sudo sed -i "/include \/etc\/nginx\/sites-enabled\/\*;/a \\\tadd_header X-Served-By \"${hostname}\";" /etc/nginx/nginx.conf',
  path        => ['/usr/bin', '/bin'],
  refreshonly => true,
  subscribe   => Exec['install_nginx'],
  notify      => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
  subscribe => Exec['configure_custom_header'],
}
