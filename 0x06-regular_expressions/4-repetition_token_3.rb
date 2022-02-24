#!/usr/bin/env ruby
# Find the regular expression
puts ARGV[0].scan(/(hbn|hbt+n)/).join
