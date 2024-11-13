import sys
from collections import Counter

def freq(s, e):
    events = []
    
    for i in range(len(s)):
        events.append((s[i], 1))
        events.append((e[i], -1))

    events.sort(key=lambda x: (x[0], x[1]))

    max_overlap = 0
    current_overlap = 0
    most_overlapping_start = None
    most_overlapping_end = None
    interval_active = False

    for time, event in events:
        current_overlap += event

        if current_overlap > max_overlap:
            max_overlap = current_overlap
            most_overlapping_start = time
            interval_active = True

        if current_overlap < max_overlap and interval_active:
            most_overlapping_end = time
            interval_active = False

    if interval_active:
        most_overlapping_end = events[-1][0]

    return max_overlap, most_overlapping_start, most_overlapping_end

def crowd(p, s, e):
    combined = list(zip(p, s, e))
    combined.sort(key=lambda x: x[0])
    p, s, e = zip(*combined)

    p = list(p)
    s = list(s)
    e = list(e)
    
    p.append(0)
    result = ['', 0, 0, 0]
    current_place = p[0]
    current_stimes = []
    current_etimes = []

    for i in range(len(p)-1):
        current_place = p[i]
        current_stimes.append(s[i])
        current_etimes.append(e[i])
        if(current_place != p[i+1]):
            #print(current_place)
            #print(current_stimes)
            #print(current_etimes)
            max_crowd, max_s, max_e = freq(current_stimes, current_etimes)
            #print("max crowd = ", max_crowd)
            if(result[0] == '' or result[3] < max_crowd):
                result = [current_place, max_s, max_e, max_crowd]
        
            current_stimes = []
            current_etimes = []

    if current_stimes and current_etimes:
        max_crowd, max_s, max_e = freq(current_stimes, current_etimes)
        if(result[0] == '' or result[3] < max_crowd):
            result = [current_place, max_s, max_e, max_crowd]


    print(result[0], end = ' ')
    print(result[1], end = ' ')
    print(result[2], end = ' ')
    
##main##
N = int(sys.stdin.readline())

data = []
places = []
names = []
stimes = []
etimes = []
length = 0
for i in range(N):
    name, place, start_time, end_time = map(str, sys.stdin.readline().split())
    if name  not in names:
        places.append(str(place))
        names.append(str(name))
        stimes.append(int(start_time))
        etimes.append(int(end_time))
        length += 1
#print(names)
#print(places)
crowd(places, stimes, etimes)