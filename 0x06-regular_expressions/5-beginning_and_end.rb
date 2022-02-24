#!/usr/bin/env ruby
# Find expression that starts with h and ends with n
puts ARGV[0].scan(/^h.n$/).join
