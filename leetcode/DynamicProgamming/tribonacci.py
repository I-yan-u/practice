class Solution:
    """
    This class provides a solution for calculating the tribonacci number for a given input.

    The tribonacci sequence is a series of numbers in which each number is the sum of the three preceding ones.
    The sequence starts with 0, 1, 1, and each subsequent number is the sum of the three preceding numbers.

    Attributes:
        None

    Methods:
        tribonacci: Calculates the tribonacci number for a given input.

    """

    def tribonacci(self, n: int) -> int:
        """
        Calculates the tribonacci number for a given input.

        Args:
            n (int): The index of the tribonacci number to be calculated.

        Returns:
            int: The tribonacci number at the given index.

        """
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        dp = [0] * (n + 1)

        dp[0], dp[1], dp[2] = 0, 1, 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
    

if __name__ == '__main__':
    import sys
    sol = Solution()
    print(sol.tribonacci(int(sys.argv[1]))) 