class Solution:
    def binaryToDecimal1(self, n: int) -> int:
        decimal = 0
        power = 1

        while n != 0:
            bit = n % 10
            if bit == 1:
                decimal = (bit * power) + decimal
            power *= 2
            n = n // 10

        return decimal
    
x = 1
a = Solution()
result1 = a.binaryToDecimal1(x)
print(result1)