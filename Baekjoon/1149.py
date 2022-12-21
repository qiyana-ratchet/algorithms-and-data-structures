N = int(input())

arr=[[0]*3 for _ in range(N)]

for i in range(N):
    arr[i][0],arr[i][1],arr[i][2] = map(int,input().split())

for i in range(N-1):
    arr[i+1][0]+=min(arr[i][1],arr[i][2])
    arr[i+1][1]+=min(arr[i][2],arr[i][0])
    arr[i+1][2]+=min(arr[i][0],arr[i][1])

print(min(arr[-1]))