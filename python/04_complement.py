class Solution:

    def complement(self, n: int) -> int:
        """
        NO: 1009
        10's complement is -11 : python
        1010 (10)'s complement is 0101 (5) : what we want

        step1: 0000001010 =complement=> 1111110101 
        step2: create mask to get only complement's original bit's value
               for `0000001010` we need `0000001111` as mask to get with & "0000000101"
        """

        if n == 0:
            return 1

        if n < 0:
            return 0

        m = n
        mask = 0

        while m != 0:
            mask = (mask << 1) | 1
            m >>= 1

        return ~n & mask 

x = 10
a = Solution()
result = a.complement(x)
print(result)


        

