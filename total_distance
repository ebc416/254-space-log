import re

def get_total_fuel(content):
	pattern = re.compile("\"FuelUsed\":(\d+\.\d+)")
	result = pattern.findall(content)
	distance = 0
	if result:
		for d in result:
			fuel+=float(d)
	return distance
