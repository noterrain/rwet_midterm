import sys
import random
import re

question = list()
for line in open('wired1.txt'):
  line = line.strip()
  line = line.replace(",", "n")
  line = line.replace(".", "\n")
  line = line.replace("!", "\n")
  line = line.replace("?", "?\n")
  line = line.replace("(", "\n")
  line = line.replace(")", "\n")
  line = line.replace("- ", "\n")
  line = line.replace('"', "\n")
  line = line.replace("[", "\n")
  line = line.replace("]", "\n")
  
  sentences = line.split("\n")
  for sentence in sentences:
    offset = sentence.find("?")
    if offset !=-1: 
      print sentence
 