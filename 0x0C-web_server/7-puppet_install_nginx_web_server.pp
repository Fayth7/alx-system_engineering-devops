# Installs Nginx Web Server

include stdlib

class nginx_config {
    package { 'nginx':
            ensure => present,
	        }

    file { '/var/www/html/index.html':
            content => 'Hello World!',
	        }

    file { '/etc/nginx/sites-available/default':
            content => '
	    server {
	        listen 80 default_server;
		    listen [::]:80 default_server;

    root /var/www/html;
        index index.html;

    location /redirect_me {
            return 301 https://www.example.com/;
	        }

    location / {
            try_files $uri $uri/ =404;
	        }
		}',
		        notify => Service['nginx'],
			    }

    service { 'nginx':
            ensure  => running,
	            enable  => true,
		            require => Package['nginx'],
			        }
				}

include nginx_config
