import sys
import random
import re
import random

proposition_list = list()

for line in open('wired1.txt'):
  line = line.strip()
  line = line.replace(",", "\n")
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
    for match_obj in re.finditer(r"\b(on .*)((which|that|where).*)", sentence):
      print match_obj.group(1)

  #  for matching_string in re.findall(r'\b[Ii]t \w+',sentence):
   #   print matching_string
 
#for line in sys.stdin:
  #line = line.strip()
 # for match_obj in re.finditer(r"\b(on|at.*)\b(which|that|who)", line):
  #for match_obj in re.finditer(r"\b(on.*)(\bwhich|that)", line):
   # print match_obj.group(1)
  