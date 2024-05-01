"""
This module provides a solution for the climbing stairs problem.
"""

class Solution:
    """
    This class provides a solution for the climbing stairs problem.
    """

    memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb to the top of the stairs.

        Args:
            n (int): The total number of stairs.

        Returns:
            int: The number of distinct ways to climb to the top of the stairs.
        """
        if n in self.memo.keys():
            return self.memo[n]
            
        solution = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = solution
        return self.memo[n]
    

if __name__ == '__main__':
    import sys
    sol = Solution()
    print(sol.climbStairs(int(sys.argv[1])))