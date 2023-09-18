#!/usr/bin/env bash
# Using puppet to make changes to config file

file { 'etc/ssh/ssh_config':
  ensure => present,

content =>"
	#ssh configuration
	host*
	identityFile ~/.ssh/school
	PasswordAuthentication no
}
