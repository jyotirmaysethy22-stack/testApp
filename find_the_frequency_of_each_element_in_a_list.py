numbers = [1, 2, 2, 3, 4, 3, 2, 5, 4, 1,"Apple",'Mango']
d = {}
for i in numbers:
    d[i] = d.get(i,0)+1
print(d)