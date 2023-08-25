#!/usr/bin/pup

# This script kills a process called killmenow

exec { 'pkill':
  provider => 'shell',
  command  => 'pkill -f killmenow',
}

