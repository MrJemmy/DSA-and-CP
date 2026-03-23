class Solution:
    def decimalToBinary1(self, n: int) -> int:
        binary = 0
        power = 1

        while n != 0:
            bit = n & 1
            binary = (bit * power) + binary
            power *= 10
            n = n >> 1

        return binary
    
    def decimalToBinary2(self, n: int) -> int:
        binary = 0
        power = 1

        while n != 0:
            bit = n % 2
            binary = (bit * power) + binary
            power *= 10
            n = n // 2

        return binary
    
x = 4
a = Solution()
result1 = a.decimalToBinary1(x)
result2 = a.decimalToBinary2(x)
print(result1)
print(result2)