#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 2020
@authors: Jorge Camarero Vera and José Jesus Gallego-Parrilla
"""


import re

class SpecieHtml:
  __fileName = None
  __contentFile = None

  def __init__(self, fileName):
    self.__fileName = fileName
    with open(fileName) as f:
      self.__contentFile = f.read()

  def getFileName(self):
    return self.__fileName

  def searchSpecie(self, speciesName):
    regexBegin = "<tr style = \"background:#[\w\d]+\"><td>WP_[\d]+\.1<\/td><td colspan = 5>(.*"
    regexEnd = ".*)<\/td><\/tr>"
    regex = regexBegin + speciesName + regexEnd
    count = sum(1 for match in re.finditer(r"{}".format(regex),
      self.__contentFile))
    return count

  def findAllSpecieNames(self):
    allSpecies = {}
    regex = "<tr style = \"background:#[\w\d]+\"><td>WP_[\d]+\.1<\/td><td colspan = 5>.*\[(.*)\]<\/td><\/tr>"
    for match in re.finditer(r"{}".format(regex), self.__contentFile):
      specie = match.group(1)
      if (specie in allSpecies):
        allSpecies[specie] += 1
      else:
        allSpecies.update({specie: 1})
    return allSpecies