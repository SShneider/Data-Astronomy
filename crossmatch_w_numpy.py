
# Write your crossmatch function here.
import numpy as np
import time
def angular_dist(r1, d1, r2, d2):
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  a = np.sin(np.abs(d1-d2)/2)**2
  d = 2*np.arcsin(np.sqrt(a + b))
  return d

def crossmatch(cat1, cat2, distIn):
    start = time.perf_counter()
    distIn = np.radians(distIn)
    cat1 = np.radians(cat1)
    cat2 = np.radians(cat2)
    ra2s = cat2[:,0]
    dec2s = cat2[:,1]
    matches = []
    nomatches = []
    for id1, cat1 in enumerate(cat1):
      dists = angular_dist(cat1[0], cat1[1], ra2s, dec2s)
      id2 = np.argmin(dists)
      closestDist = dists[id2]
      if closestDist<=distIn:
        matches.append((id1, id2, np.degrees(closestDist)))
      else:
        nomatches.append(id1)
    return (matches, nomatches, time.perf_counter() - start)
