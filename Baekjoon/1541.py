word = input()
num = ""
num_arr = []
equations_arr = []
for letter in word:
    if letter != "-" and letter != "+":
        num += letter
    if letter == "+":
        num_arr.append(int(num))
        num = ""
        equations_arr.append("+")
    if letter == "-":
        num_arr.append(int(num))
        num = ""
        equations_arr.append("-")
num_arr.append(int(num))

answer = num_arr[0]
tmp = 0
is_minus = False

for i in range(len(equations_arr)):
    if equations_arr[i] == "+" and not is_minus:
        answer += num_arr[i+1]
    elif equations_arr[i] == "+" and is_minus:
        tmp += num_arr[i+1]
    elif equations_arr[i] == "-" and not is_minus:
        is_minus = True
        tmp += num_arr[i+1]
    elif equations_arr[i] == "-" and is_minus:
        answer -= tmp
        tmp = 0
        answer -= num_arr[i+1]
answer -= tmp
print(answer)