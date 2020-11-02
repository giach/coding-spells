def plusOne(A):
        number = 0

        for i in A:
            number = number * 10 + i

        print(number)

        newnr = number + 1

        newarr = []
        while newnr != 0:
            newarr.append(newnr % 10)
            newnr = newnr / 10

        print(type(newarr))
        return newarr[::-1]

# result = plusOne([0])
result = plusOne([ 2, 5, 6, 8, 6, 1, 2, 4, 5 ])

print(range(4, 0, -1))

print(result)