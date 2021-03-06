#!/usr/bin/env python3
#
# Use like `./space_log.py -s|-p|-t|-d|-f log_file

from sys import argv
import fuel
import planet_list
import planets_scanned
import Question3
import total_distance

# Opens the log file and grabs the contents.
try:
	fh = open(argv[1], 'r')
	content = fh.read()
	fh.close()
except IndexError:
	exit("Missing name of log file.")
except:
	exit("Couldn't open file \""+argv[1]+"\".")

# Uncomment, and add your work in the appropriate spots.
argSwitcher = {
	'-s': planet_list.Names_of_system_visted,
	'-p': planets_scanned.scanned_planets,
	'-t': Question3.is_it_terraformable,
	'-d': total_distance.get_total_distance,
	'-f': fuel.get_total_fuel,	# The example.
}

try:
	func = argSwitcher.get(argv[2], lambda x: "Incorrect search argument.")
except IndexError:
	exit("Missing search argument.")
output = func(content)
if type(output) is list:
	for l in output:
		print(l)
else:
	print(output)
