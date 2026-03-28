class Solution:

    def factorial(self, n: int) -> int:

        fact = 1

        for i in range(1, n+1):
            fact *= i

        return fact

    def nCr(self, n: int, r: int) -> int:
        """
        nCr = n! / r! * (n-r)!
        """

        num = self.factorial(n)
        deno = self.factorial(r) * self.factorial(n-r)

        return num/deno


a = Solution().nCr(8, 0)
print(a)