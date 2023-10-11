# 0-strace_is_your_friend.pp

# Puppet manifest to fix Apache 500 error

exec {'/etc/php5/apache2/php.ini':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/display_errors = Off/display_errors = On/g' /etc/php5/apache2/php.ini",
}

exec { '/var/www/html/wp-setting.php':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
}

exec {'/etc/init.d/apache2':
  path    => ['/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => '/etc/init.d/apache2 restart',
}
