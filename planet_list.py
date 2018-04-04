#Efrain Bonilla Caudillo 
import re

def Names_of_system_visted(content):
    pattern = re.compile(r"\"event\":\"FSDJump\", \"StarSystem\":\"(\w+\s\w+[-\s]\w+[-\s]\w+[-\s\w]\"?\w?\w?\w?\w?\s?\w?-?\w?-?\w?\w?)\"?")  
    matches = pattern.finditer(content)
    for match in matches:
        print(match.group(1))
