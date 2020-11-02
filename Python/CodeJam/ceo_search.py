class Solution:

    def main(self):
        T = int(input())
        for i in range(0,T):
            L = int(input())
            line = input().split()
            prev_emp = int(line[0])
            prev_exp = int(line[1])
            carrier = 0        

            #edge case
            if L == 1:
                exp = prev_emp + 1
                print("Case #{}: {}".format(i+1, exp))
                continue
            
            for j in range(1,L):
                line = input().split()
                emp = int(line[0])
                exp = int(line[1])
                if (emp * exp) < (prev_emp + carrier):
                    carrier = (prev_emp + carrier) - (emp * exp)
                else:
                    carrier = 0
                prev_emp = emp

            exp += 1
            while (carrier - exp) > 0:
                carrier -= exp
                exp += 1

            print("Case #{}: {}".format(i+1, exp))

x = Solution()
x.main()
