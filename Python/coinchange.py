def print_matrix(m):
    idx = 1
    for r in m:
        if idx < 10:
            print(" ", idx, r)
        else:
            print(idx, r)
        idx += 1
    print("-------------------")


def nz_min(line):
    if len(line) == 0:
        return 0
    line = [i for i in line if i != 0]

    if len(line) == 0:
        return 0
    else:
        return min(line)

def min_val(x, y):
        if y == 0:
            return x
        if x > y:
            return y
        return x

def coinChange(coins, amount):
    rows = amount
    cols = len(coins)
    arr = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        if (i+1) % coins[0] == 0:
            arr[i][0] = (i+1) // coins[0]

    print_matrix(arr)

    for i in range(1,cols):
        for j in range(rows):
            part_amt = (j + 1)
            if part_amt < coins[i]:
                arr[j][i] = arr[j][i-1]
            else:
                x = part_amt // coins[i]
                y = part_amt %  coins[i]

                mval = 9999
                if y == 0:
                    mval = min_val(mval, x)

                mval = min_val(mval, arr[j][i-1])

                idx = part_amt - coins[i] * 1 - 1
                if arr[idx][i] != 0:
                    mval = min_val(mval, 1 + arr[idx][i])
                arr[j][i] = mval
        print_matrix(arr)
    return nz_min(arr[-1])


print(coinChange([2,5,10,1], 27))
