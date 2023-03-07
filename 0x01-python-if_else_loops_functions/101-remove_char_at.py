#!/usr/bin/python3
def remove_char_at(str, n):
	copy = str[:n] + str[n+1:]
	print(copy)

remove_char_at("indigo", 4)
