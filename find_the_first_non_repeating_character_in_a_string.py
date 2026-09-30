string = "Pprocess fiPnished with exit code"

# Method -1
for i in range(len(string)):
    c = 0
    for j in string:
        if string[i] == j:
            c= c +1
    if c <= 1:
        print(string[i])
# Find the first non-repeating character in a string. -
# Method - 2
for char in string:
    if string.count(char) == 1:
        print("First non-repeating character:", char)
        break