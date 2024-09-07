# https://leetcode.com/problems/sort-an-array/
# Quick sort: 
#   average: O(nlogn)
#   worst: O(n^2): pivot is always at the edge
#   best: O(n): array the same
# Merge sort:
#   always: O(nlogn)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.mergeSort(nums, 0, len(nums))
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    # hi: high index
    def quickSort(self, nums, lo, hi):
        if lo >= hi:
            return

        def partition(lo, hi):
            nonlocal nums
            pivot = nums[random.randint(lo, hi)]
            p1, i, p2  = lo, lo, hi # []p1 p2[]
            while i <= p2:
                if nums[i] < pivot:
                    nums[i], nums[p1] = nums[p1], nums[i]
                    p1 += 1
                    i += 1 # e before i is always < pivot
                elif nums[i] > pivot:
                    nums[i], nums[p2] = nums[p2], nums[i]
                    p2 -= 1
                else:
                    i += 1

            return p1, p2

        p1, p2 = partition(lo, hi) # [less]p1 p2[greater]
        self.quickSort(nums, lo, p1 - 1)
        self.quickSort(nums, p2 + 1, hi)
    
    # hi: higher bound
    def mergeSort(self, nums: List[int], lo, hi):
        n = hi - lo
        if n == 1: return [nums[lo]]
        if n == 2:
            if nums[lo] < nums[lo + 1]:
                return [nums[lo], nums[lo + 1]]
            return [nums[lo + 1], nums[lo]]
        
        mid = (lo + hi) // 2
        sorted1 = self.mergeSort(nums, lo, mid)
        sorted2 = self.mergeSort(nums, mid, hi)
        return self.merge(sorted1, sorted2)

    def merge(self, sorted1, sorted2):
        merged = [None] * (len(sorted1) + len(sorted2))
        p1, p2, i = 0, 0, 0
        while p1 < len(sorted1) and p2 < len(sorted2):
            if sorted1[p1] < sorted2[p2]:
                merged[i] = sorted1[p1]
                p1 += 1
            else:
                merged[i] = sorted2[p2]
                p2 += 1
            i += 1
        self.fill(merged, i, sorted1, p1)
        self.fill(merged, i, sorted2, p2)

        return merged
    
    def fill(self, merged, i, sorted_arr, p):
        while p < len(sorted_arr):
            merged[i] = sorted_arr[p]
            i += 1
            p += 1