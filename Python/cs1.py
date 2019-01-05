# arr = [10,15,7,8]
# k = 17

arr = [1,4,45,6,10,-8]
k = 16

dit = {}

for x in arr:
    r = k - x
    elem = dit.get(x)
    if elem is None:
        dit[r] = r
    else:
        print(x,r)
        break
