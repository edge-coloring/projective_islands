# %%
def generateTuples(rep: int, ring: int):
    dists: set[tuple] = set()
    def tryToInsertDist(dist: tuple):
        for i in range(rep*2):
            d = tuple(dist[i:] + dist[:i])
            if d in dists: return
        for i in range(rep*2):
            d = tuple(dist[::-1][i:] + dist[::-1][:i])
            if d in dists: return
        dists.add(dist)
    def dfsAllDists(rem, stack: list):
        if len(stack) == rep*2:
            if rem == 0:
                tryToInsertDist(tuple(stack))
            return
        for x in range(rem+1):
            dfsAllDists(rem - x, stack + [x])
    dfsAllDists(ring, [])
    sortedDists = sorted(list(dists))
    filteredDists = []
    for dist in sortedDists:
        distdist = list(dist) + list(dist)
        bad = False
        for l in range(len(dist)//2):
            if dist[l]+dist[l+rep] == 0:
                bad = True
                break
        else:
            for l in range(rep*2):
                for x in range(2, rep):
                    if sum(distdist[l:l+x]) <= x-2:
                        bad = True
        if not bad:
            filteredDists.append(dist)
    return filteredDists
# %%
def generateDConfFromTuple(dist: tuple, rep: int, ring: int):
    dconf = []
    assert(len(dist) == rep*2)
    assert(sum(dist) == ring)
    ringSurface = []
    cnt = 0
    for d in dist:
        es = []
        for _ in range(d+1):
            e = rep+ring+cnt
            es.append(e)
            cnt += 1
        ringSurface.append(es)
    for v in range(rep*2):
        left = ringSurface[v-1][-1]
        right = ringSurface[v][0]
        center = ring+(v%rep)
        dconf.append((left, right, center))
    v = 0
    for sect in range(rep*2):
        for index in range(len(ringSurface[sect])-1):
            left = ringSurface[sect][index]
            right = ringSurface[sect][index+1]
            outer = v
            dconf.append((left, right, outer))
            v += 1
    return dconf
# %%
import os
def outputRepRingDConfs(rep: int, ring: int):
    dirName = f"{rep}-{ring}"
    os.mkdir(dirName)
    dirName += "/dconf"
    os.mkdir(dirName)
    dists = generateTuples(rep, ring)
    for dist in dists:
        fileName = ""
        for d in dist:
            fileName += chr(ord('0')+d)
        fileName += ".dconf"
        with open(os.path.join(dirName, fileName), "w") as f:
            dconf = generateDConfFromTuple(dist, rep, ring)
            vNum = rep*2 + ring
            f.write(f"{vNum} {ring}\n")
            for (a, b, c) in dconf:
                f.write(f"{a} {b} {c}\n")

# %%
outputRepRingDConfs(3, 6)
outputRepRingDConfs(3, 7)
outputRepRingDConfs(3, 8)
outputRepRingDConfs(4, 6)
outputRepRingDConfs(4, 7)
outputRepRingDConfs(4, 8)
outputRepRingDConfs(5, 8)
outputRepRingDConfs(5, 9)
outputRepRingDConfs(5, 10)
outputRepRingDConfs(5, 11)
outputRepRingDConfs(5, 12)
outputRepRingDConfs(5, 13)