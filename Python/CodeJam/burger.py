class Solution:

    def main(self):
        t = int(input())
        for i in range(1, t + 1):
            n = int(input())
            d = [int(s) for s in input().split(" ")]
            opt = []
            s = int(n / 2)
            for j in range(0,s):
                opt.append(j)
                opt.append(j)
            if n % 2 == 1:
                opt.append(s)

            d.sort()
            error = 0
            for e1,e2 in zip(opt,d):
                error += (e1 - e2) * (e1 - e2)
            print("Case #{}: {}".format(i, error))

x = Solution()
x.main()
