#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:30:19 2020
__author__ = 'Jose Jesus Gallego-Parrilla'
__license__ = "GPL"
__maintainer__ = "Jose Jesus Gallego-Parrilla"
__email__ = "J.J.Gallego-Parrilla2@newcastle.ac.uk"
"""

while True:
    try:
        answer = int(input("Press 1 to see protein ID in console \nPress 2 to export protein CSV list \nChoose="))
        if answer == 1 or answer == 2:
            break
    except ValueError:
        pass
    print("Sorry, not what I was expecting \nTry again")
if answer== 1:
    from ProteinHtmlID import ProteinHtmlID 

    if __name__ == "__main__":
        protein = ProteinHtmlID("chandra.html") #name of the file you want check
        name = protein.getFileName()
        print(name)
    
        count = protein.searchProtein("Acidobacterium ailaaui")
        print(count)
    
        found = protein.findAllProteinNames()
        print(found)
elif answer== 2:
    import pandas as pd
    from ProteinHtmlID import ProteinHtmlID 
    
    #prot_name = ProteinHtmlID("chandra.html")
    wp_num = ProteinHtmlID("chandra.html")
    
    #found = prot_name.findAllProteinNames()
    found = wp_num.findAllProteinNames()
    
    #prot_name = []
    places = []
    wp_num = []
    
    for elem in found:
      #prot_name.append(elem)
      wp_num.append(elem)
      places.append(found[elem])
      
    
    #data = {'Name' : prot_name, 'Place' : places, 'ID' : wp_num}
    data = {'Place' : places, 'ID' : wp_num}
    dataframe = pd.DataFrame(data)
    df = pd.DataFrame(data)
    df.to_csv('Tat_related.csv', index=False) #name for exported document
    print(dataframe)
