# Write your mean_datasets function here
import numpy as np
import math
def mean_datasets(*args):
  data = []
  count = 0
  for fileIn in args[0]:
    if(not len(data)):
      data = np.loadtxt(fileIn, delimiter=',')
    else:
      data = np.add(data, np.loadtxt(fileIn, delimiter=','))
  #data = np.loadtxt(args[0], delimiter=',')

   
#    count = 0
#    for line in open(fileIn):
#      data[count] = (line.strip().split(','))

  #print(data)
  return np.round(data/len(args[0]), 1)
