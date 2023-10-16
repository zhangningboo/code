n, m = map(int, input().split(' '))

class LinkNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None

cur = head = LinkNode(1)

for i in range(2, n + 1):
    tmp = LinkNode(i)
    cur.next = tmp
    cur = tmp

cur.next = head

pre = cur
cur = head

res = []
while cur != cur.next:
    for _ in range(1, m):
        pre = cur
        cur = cur.next    
    res.append(cur.val)
    pre.next = cur.next
    cur = pre.next
res.append(cur.val)

print(' '.join(map(str, res)))