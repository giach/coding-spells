class Solution:

    def isDesirableP(self, a, b, c):
        if a > b and c > b:
            return True
        if b > a and b > c:
            return True
            
        return False
    
    def isDesirable(self,arr):
        size = len(arr)
        if size < 3:
            return False

        w = arr[0]
        e = arr[-1]

        return self.isDesirableP(w,arr[-2],e) or self.isDesirableP(w, arr[2], e) or self.isDesirable(arr[1:]) or self.isDesirable(arr[:-1])
        

    def main(self):
        T = int(input())
        for i in range(0,T):
            K = int(input())
            marks = input().split()
            
            posts = 0
            
            P = self.isDesirable(marks)
            print(P)

            # print("Case #{}: {}".format(i+1, posts)
        
        P = self.isDesirable([1,2,3,4])
        print(P)

x = Solution()
x.main()
