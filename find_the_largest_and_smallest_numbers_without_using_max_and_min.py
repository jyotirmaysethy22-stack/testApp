numbers = [1, 2, 2, 3, 4, 3, 2, 5, 4, -1]
mx = numbers[0]
mn = numbers[0]

for i in numbers:
    if i > mx:
        mx = i
    elif i < mn :
        mn = i
print(mx,mn)

# op- 5 -1