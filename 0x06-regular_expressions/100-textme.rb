#!/usr/bin/env ruby
sender = ARGV[0].scan(/from:(\+?\w+)/).join
recevier = ARGV[0].scan(/to:(\+?\d{11})/).join
flags = ARGV[0].scan(/\[flags:([^\]]+)\]/).join
puts "#{sender},#{recevier},#{flags}"
