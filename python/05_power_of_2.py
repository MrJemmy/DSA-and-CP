class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        No.: 231
        n = 32
        check from 2 * 2 is it 32 then repeat till value cross(false) or match(true)

        "how to handle -ve values"

        """
        # INT_MAX = 2147483647 # (2**(msize-1))-1 := here msize = 32
        powerOfTwo = 1
        
        while n >= powerOfTwo:
            
            if powerOfTwo == n:
                return True
            
            # if powerOfTwo > INT_MAX/2: # limit for memory cap
            #     powerOfTwo *= 2 
            powerOfTwo *= 2 # powerOfTwo << 1 ?

        return False
    
    def isPowerOfTwoOpt(self, n: int) -> bool:
        """
        if it's power of 2 then it will have only one 1bit other are as 0big for positive
        """
        pass

a = Solution().isPowerOfTwo(-1)
print(a)