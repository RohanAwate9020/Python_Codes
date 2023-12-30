class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        sum=0
        for i in bills:
            if i==5:
                sum=sum+5
                state=True
            elif i>5:
                j=i
                K=j-5
                if K<=sum:
                    state=True
                    sum=sum-K
                    j=0
                    K=0
                    sum=sum+5
                else:
                    state=False
   
#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends