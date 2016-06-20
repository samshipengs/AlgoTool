# Uses python3
import sys
from collections import namedtuple
import numpy as np
import copy

Segment = namedtuple('Segment', 'start end')

# def optimal_points(segments):
#     segments.sort(key=lambda x:x[0])
#     points = []
#     seg_cp = copy.deepcopy(segments)
#     for i in range(len(segments)-1):
#         if segments[i] in seg_cp:
#             for j in range(i+1, len(segments)):
#                 if (segments[i].end >= segments[j].start) and (segments[i].end<=segments[j].end) \
#                 and (segments[j] in seg_cp):
#                     points.append(segments[i].end)
#                     print(segments[i].end)
#                     seg_cp.remove(segments[j])
#                 elif (segments[i].end >= segments[j].start) and (segments[i].end>=segments[j].end) \
#                 and (segments[j] in seg_cp):
#                     points.append(segments[j].end)
#                     print(segments[j].end)
#                     seg_cp.remove(segments[j])
#     return list(set(points))

def optimal_points(segments):
    segments.sort(key=lambda x:x[1]) # sort according to right end pts
    seg_cp = copy.deepcopy(segments)
    pts = []
    for i in range(len(segments)-1):
        if segments[i] in seg_cp:
            pts.append(segments[i].end)
            for j in range(i+1, len(segments)):
                if (segments[j].start <= segments[i].end) and (segments[j] in seg_cp):
                    seg_cp.remove(segments[j])
    # deal with last interval
    if pts[-1] < segments[-1].start:
        pts.append(segments[-1].end)
    return list(set(pts))



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
