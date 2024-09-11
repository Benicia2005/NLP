import inflect
p = inflect.engine()
def pluralize(noun):
    return p.plural(noun)
print(pluralize("cat"))
print(pluralize("dog")) 
print(pluralize("child"))  
