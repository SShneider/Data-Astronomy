import numpy as np
def angular_dist(r1, d1, r2, d2):
  d1=np.radians(d1)
  r1=np.radians(r1)
  d2=np.radians(d2)
  r2=np.radians(r2)
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  a = np.sin(np.abs(d1-d2)/2)**2
  d = 2*np.arcsin(np.sqrt(a + b))
  d=np.degrees(d)
  return d
def hms2dec(hrIn, minIn, secIn):
  return (15*(hrIn+minIn/60+secIn/3600))
def dms2dec(degIn, aminIn, asecIn):
  return (abs(degIn)+aminIn/60+asecIn/3600)*(degIn/abs(degIn))
def import_super():
  superList = []
  readSuper = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  for idx, val in enumerate(readSuper):
    superList.append((idx+1, val[0], val[1]))
  return superList
def import_bss():
  bssList = []
  readBss = np.loadtxt('bss.dat', usecols=range(1, 7))
  for idx, val in enumerate(readBss):
    bssList.append((idx+1, hms2dec(val[0],val[1], val[2]), dms2dec(val[3], val[4], val[5])))
  return bssList
def find_closest(catIn, d2, r2):
  idOut = 0
  minDist = 361
  for entry in catIn:
    distComp = angular_dist(entry[1], entry[2], d2, r2)
    if distComp<minDist:
      minDist = distComp
      idOut = entry[0]
  return (idOut, minDist)

def crossmatch(bssIn, superIn, distIn):
    matches = []
    nomatches = []
    for entryBSS in bssIn:
      closest = find_closest(superIn, entryBSS[1], entryBSS[2])
      if closest[1]<distIn:
        matches.append((entryBSS[0], closest[0], closest[1]))
      else:
        nomatches.append(entryBSS[0])
    return (matches, nomatches)
      
