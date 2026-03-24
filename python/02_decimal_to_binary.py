class Solution:
    def decimalToBinary(self, n: int, m_size: int = 8) -> int:

        if n < 0:
            # -10 => 10 ignore -ve
            # 1's complement which is ~ binary not opration on 10
            # add 1 result in binary for -10
            n = ~abs(n)+1

        binary = 0
        power = 1
        count = m_size # require for -ve

        while n != 0 and count !=0:
            bit = n & 1 # n - 10 * int(n / 10) => n % 10
            binary = (bit * power) + binary
            power *= 10
            n = n >> 1 # int(n / 10) =>  n //= 10
            count -= 1
        return binary
    
x = 4
a = Solution()
result = a.decimalToBinary(x)
print(result)