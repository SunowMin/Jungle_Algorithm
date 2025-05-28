import sys
input = sys.stdin.readline

heap = []

N = int(input())

def insert(x):
    heap.append(x)
    idx = len(heap) - 1
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[idx] > heap[parent]:
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break

def delete():
    if not heap:
        return 0
    max_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    idx = 0
    while True:
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx
        if left < len(heap) and heap[left] > heap[largest]:
            largest = left
        if right < len(heap) and heap[right] > heap[largest]:
            largest = right
        if largest == idx:
            break
        heap[idx], heap[largest] = heap[largest], heap[idx]
        idx = largest
    return max_val

for _ in range(N):
    x = int(input())
    if x == 0:
        print(delete())
    else:
        insert(x)
