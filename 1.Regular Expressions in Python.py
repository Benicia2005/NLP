import re
pattern=r'\b[a-zA-Z]+\b'
text="Hello, World!"
matches=re.findall(pattern,text)
print(matches)
