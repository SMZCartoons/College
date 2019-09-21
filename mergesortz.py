#a.pop(0) takes the first value of a list
a = [1, 2, 4, 9, 10]
b = [3, 5, 6, 7, 8]
c = []
for x in range (10):
    if len(a) == 0:
        c += b
        print(c)
        break
    if len(b) == 0:
        c+= a
        print(c)
        break
    if a<b:
        c.append(a.pop(0))
    if a>b:
        c.append(b.pop(0))
        