#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:20:38 2020

@author: Jorge Camarero Vera and José Jesus Gallego-Parrilla
"""

import pandas as pd
from SpecieHtml import SpecieHtml 

specie = SpecieHtml("chandra.html")

found = specie.findAllSpecieNames()

names = []
places = []

for elem in found:
  names.append(elem)
  places.append(found[elem])

data = {'Name' : names, 'Place' : places}
dataframe = pd.DataFrame(data)
df = pd.DataFrame(data)
df.to_csv('Species_sorter2.csv', index=False)
print(dataframe)