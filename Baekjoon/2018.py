N = int(input())
answer = 0
i = 0
j = 0
sum_between = 0

while(True):
    if j > N:
        break
    if sum_between < N:
        j += 1
        sum_between += j
    elif sum_between > N:
        sum_between -= i
        i += 1
    elif sum_between == N:
        answer += 1
        j+=1
        i+=1
        sum_between += j+1-i

print(answer)