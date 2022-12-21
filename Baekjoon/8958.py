N = int(input())

for i in range(N):
    word = input()
    answer = 0
    count = 0
    for letter in word:
        if letter == "O":
            count += 1
            answer += count
        else:
            count = 0
    print(answer)
