#!/usr/bin/env ruby

# Extract sender, receiver, and flags from the text message into match
match = ARGV[0].match(/\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/)

# Output the result
puts "#{match[1]},#{match[2]},#{match[3]}"
