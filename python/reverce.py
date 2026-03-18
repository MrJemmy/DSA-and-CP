class Solution:
    def __init__(self):
        self.MAX_SIZE = (2**31)-1
        self.MIN_SIZE = -(2**31)
        print(self.MIN_SIZE, 987654321)

    def reverse(self, x: int) -> int:
        ans = 0
        
        while(x!=0):
            print("x:",x, end=" ")
            # digit = x % 10 # can't use 
            digit = 10 * int(x / 10)
            # digit = int(math.fmod(x, 10))

            print("digit:",digit, end=" ")
            x = int(x / 10)
            print("new x:", x)

            if (self.MAX_SIZE/10) < ans or ans < (self.MIN_SIZE/10):
                return 0
            
            ans = (ans * 10) + digit
        return ans

        
        
a = Solution()
print("ANS:", a.reverse(-123))