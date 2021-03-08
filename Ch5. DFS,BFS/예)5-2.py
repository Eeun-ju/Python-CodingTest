from collections import deque

queue = deque()

# 8 steps +5 + 2+3 +7 - +1 +4 -

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
print(list(queue))
queue.reverse()
print(queue)
