from collections import deque

dq = deque([1, 2, 3])
print(dq)
dq.appendleft(5)
dq.appendleft(8)
dq.pop()
print(dq)
