#!/usr/bin/env python3
#
# Use like `./space_log.py -s|-p|-t|-d|-f log_file

from sys import argv
<<<<<<< HEAD
import fuel
import planet_list
=======
import fuel, re, planet_list
>>>>>>> 1b1a03a4fdf12e8f4165d9463ba46778e5527e6c

# Opens the log file and grabs the contents.
try:
	fh = open(argv[1], 'r')
	content = fh.read()
	fh.close()
except IndexError:
	exit("Missing name of log file.")
except:
	exit("Couldn't open file \""+argv[1]+"\".")

<<<<<<< HEAD
# Uncomment, and add your work in the appropriate spots.
argSwitcher = {
	'-s': planet_list.Names_of_system_visted,
=======
# Uncomment and your work in the appropriate spots.        
argSwitcher = {
	'-s': planet_list.Names_of_system_visted, #NAMES OF SYSTEMS VISITED        
>>>>>>> 1b1a03a4fdf12e8f4165d9463ba46778e5527e6c
#	'-p': NAMES OF PLANETS SCANNED
#	'-t': TOTAL NUMBER OF TERRAFORMABLE PLANETS SCANNED
#	'-d': TOTAL DISTANCE IN LIGHT YEARS
	'-f': fuel.get_total_fuel,	# The example.
}

try:
	func = argSwitcher.get(argv[2], lambda x: "Incorrect search argument.")
except IndexError:
	exit("Missing search argument.")

<<<<<<< HEAD
output = func(content)
if type(output) is list:
	for l in output:
		print(l)
else:
	print(output)
=======
print(func(content))    

>>>>>>> 1b1a03a4fdf12e8f4165d9463ba46778e5527e6c
