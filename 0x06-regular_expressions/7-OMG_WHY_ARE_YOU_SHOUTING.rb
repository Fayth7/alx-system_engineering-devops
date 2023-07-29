#!/usr/bin/env ruby

input = ARGV[0]
pattern = /[A-Z]/

matches = input.scan(pattern)
puts matches.join
