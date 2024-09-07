# https://leetcode.com/problems/count-primes/
# O(n log log n) - https://stackoverflow.com/a/2582776/6921058
from math import sqrt

MAX = 5 * 10**6
isPrime = [True] * (MAX + 1)

isPrime[0] = False
isPrime[1] = False

for i in range(2, int(sqrt(MAX) + 1)):
    if not isPrime[i]:
        continue
    for multiple in range(i * i, MAX, i):
        isPrime[multiple] = False

class Solution:
    def countPrimes(self, n: int) -> int:
        return sum(isPrime[:n])