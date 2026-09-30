my_list = [10, 10.5, 3+4j, "Jai Maa Kali", True, None, [1, 2, 3], (1, 2, 3), {1, 2, 3},10, {"name": "Jai"}, range(5)]
l2= []
for i in range(len(my_list)):
    c = 0
    for j in my_list:
        if my_list[i] == j:
            c = c +1
    if c >1 and my_list[i] not in l2:
        print("THe duplicate : ",my_list[i])
        l2.append(my_list[i])

print(l2)