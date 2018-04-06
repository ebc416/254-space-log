#Efrain Bonilla Caudillo 
import re

def Names_of_system_visted(content):
    pattern = re.compile(r"\"event\":\"FSDJump\", \"StarSystem\":\"(\w+\s\w+[-\s]\w+[-\s]\w+[-\s\w]\"?\w?\w?\w?\w?\s?\w?-?\w?-?\w?\w?)\"?")  
<<<<<<< HEAD
    matches = pattern.findall(content)
    for match in matches:
        return (matches)
=======
    matches = pattern.finditer(content)
    for match in matches:
        print(match.group(1))
>>>>>>> 1b1a03a4fdf12e8f4165d9463ba46778e5527e6c
