#Eric Minh Hanh Nguyen
#Yeah, I noticed once I was done, it was eeriely similiar to your own. Took me a lot longer to figure out how to add the numbers together
#than I'd like to admit.
#P.S. I literally took the fuel.py and put in the pieces where mine was different because I was curious how closely similiar they were.
#SPENT 1.5-2 HOURS FOR SOMETHING THAT WAS JUST ABOUT THE SAME, but yeah, doing it blind was nice, good times.
import re

def get_total_distance(content):
	pattern = re.compile("\"JumpDist\":(\d+\.\d+)")
	result = pattern.findall(content)
	distance = 0
	if result:
		for d in result:
			distance+=float(d)
	return distance
