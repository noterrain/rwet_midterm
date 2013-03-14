import sys
import random
import re

declarative = list()
for line in open('wired1.txt'):
  line = line.strip()
  line = line.replace(",", "n")
  line = line.replace(".", "\n")
  line = line.replace("?", "?\n")
  line = line.replace("!", "\n")
  line = line.replace("(", "\n")
  line = line.replace(")", "\n")
  line = line.replace("- ", "\n")
  line = line.replace('"', "\n")
  line = line.replace("[", "\n")
  line = line.replace("]", "\n")
  
  sentences = line.split("\n")
  for sentence in sentences:
    for match_obj in re.finditer(r"\b(I[i]t .*)(\bwhere|that|which\b.*)", sentence):
      print match_obj.group(1)


    #if re.search(r"?", sentence)
     # print sentence
 