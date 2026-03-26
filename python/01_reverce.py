class Solution:
    def __init__(self, msize: int = 32):
        self.MAX_SIZE = (2**(msize-1))-1
        self.MIN_SIZE = -(2**(msize-1))

    def reverse(self, x: int) -> int:
        ans = 0
        
        while(x!=0):
            # we can reuse int(x / 10)
            # digit = x % 10 # can't use 
            digit = x - 10 * int(x / 10)
            # digit = int(math.fmod(x, 10))

            x = int(x / 10)

            if (self.MAX_SIZE/10) < ans or ans < (self.MIN_SIZE/10):
                return 0
            
            ans = (ans * 10) + digit
        return ans

        
        
a = Solution()
print("ANS:", a.reverse(-12))