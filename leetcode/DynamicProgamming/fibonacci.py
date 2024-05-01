"""
This module provides a solution for calculating the nth Fibonacci number.
"""

class Solution:
    def fib(self, n: int) -> int:
        """
        Calculates the nth Fibonacci number.

        Args:
            n (int): The index of the Fibonacci number to calculate.

        Returns:
            int: The nth Fibonacci number.

        """
        if n <= 1:
            return n

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    

if __name__ == '__main__':
    import sys
    sol = Solution()
    print(sol.fib(int(sys.argv[1])))