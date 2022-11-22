from itertools import combinations
import time

x = [1,2,3,4,5,6,7,8,9,0]
time_start = time.time()
l = list(combinations(x, 4))
time_end = time.time()
for k in l:
    print(k)

print(f"\n{(time_end-time_start)}\n{len(l)}")