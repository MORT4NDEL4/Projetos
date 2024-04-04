num = [-5, 5000, 85, -1000, 54, 0, 15, -45, 12, 24, -1, 2]

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[j] < num[i]:
            num[i], num[j] = num[j], num[i]

print(num)
