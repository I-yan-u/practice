#!/usr/bin/python3
"""
Using dynamic programming approach
Utilizing Memoization and recursion
"""

import time
import sys
import json

def min_none(a: int|None, b: int|None) -> int:
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

memo = {}
def minimum_coins(m: int, coins: list[int]) -> int:
    if m in memo:
        return memo[m]

    if m == 0:
        result = 0
    else:
        result = None
        for coin in coins:
            remainder = m - coin
            if remainder < 0:
                continue
            else:
                result = min_none(result, minimum_coins(remainder, coins)+1)
    memo[m] = result
    return result


start = time.perf_counter()

amount = int(sys.argv[1])
coins = json.loads(sys.argv[2])

print(f'Amount = {amount} Type = {type(amount)},\nCoins = {coins} Type = {type(coins)}')
print(f'Min coins is {minimum_coins(amount, coins)}\n Finished in {time.perf_counter() - start:.8f}s')
#print(memo)
