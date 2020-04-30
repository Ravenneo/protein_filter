#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def countWords(address, word):
    logfile = open(address, "r")
    wordcount = 0
    for lines in logfile:
        if word in lines.split():
            wordcount += 1
    return wordcount

import re

with open("chandra.html") as f:
    contents = f.read()
    count = sum(1 for match in re.finditer(r"\bhydrogenase", contents))
    print("Hidrogenases:", count)

with open("chandra.html") as f:
    contents = f.read()
    count = sum(1 for match in re.finditer(r"\bdehydrogenase", contents))
    print("Dehidrogenases:", count)
    
with open("chandra.html") as f:
    contents = f.read()
    count = sum(1 for match in re.finditer(r"\bhypothetical.", contents))
    print("Hypothetical proteins:", count)
    
with open("chandra.html") as f:
    contents = f.read()
    count = sum(1 for match in re.finditer(r"\bprotease", contents))
    print("Proteases:", count)

with open("chandra.html") as f:
    contents = f.read()
    count = sum(1 for match in re.finditer(r"\bexopolysaccharide", contents))
    print("Exopolysaccharide biosynthesis protein:", count)
    
with open("chandra.html") as f:
    contents = f.read()
    count = sum(1 for match in re.finditer(r"\bcellulose.", contents))
    print("Cellulose related proteins:", count)