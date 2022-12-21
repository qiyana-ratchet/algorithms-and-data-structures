N, M, B = map(int, input().split())

land = []
# for i in range(N):
#     land.append(list(map(int, input().split())))
#
# merged = list(set([item for _ in land for item in _]))
for i in range(N):
    land.extend(list(map(int, input().split())))
# print(land)
land_set = list(set(land))
# print(land_set)

cost = 0
arr = []
for i in land_set:
    inventory = B
    cost = 0
    for v in land:
        if v > i:
            cost += 2 * (v - i)
            inventory += (v - i)
        if v < i:
            cost += 1 * (i - v)
            inventory -= (i - v)
    if inventory > 0:
        arr.append((cost,i))
    # print(arr)
arr.sort(key=lambda x: (x[0], x[1]))
print(arr[0][0],arr[0][1])
