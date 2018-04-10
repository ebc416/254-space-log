import re

def get_total_distance(content):
	pattern = re.compile("\"JumpDist\":(\d+\.\d+)")
	result = pattern.findall(content)
	distance = 0
	if result:
		for d in result:
			distance+=float(d)
	return distance
