#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created onMay 2020

@author: Jorge Camarero Vera and José Jesus Gallego-Parrilla
"""

from SpecieHtml import SpecieHtml 

if __name__ == "__main__":
    specie = SpecieHtml("chandra.html") #name of the file you want check
    name = specie.getFileName()
    print(name)

    count = specie.searchSpecie("Acidobacterium ailaaui")
    print(count)

    found = specie.findAllSpecieNames()
    print(found)