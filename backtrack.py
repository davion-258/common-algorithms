# https://leetcode.com/problems/combinations/
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        arr = [None] * k
        
        def backtrack(arr_pos, cur_num):
            if arr_pos == k:
                ans.append(arr[:]) # Copy arr
                return
            unfilled_len = k - arr_pos - 1
            for i in range(cur_num, n - unfilled_len + 1):
                arr[arr_pos] = i # fill num at arr_pos
                backtrack(arr_pos + 1, i + 1) # fill num at the left positions
        backtrack(0, 1)
        return ans
        