class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        total = 0

        for num in nums:
            total += num
            arr.append(total)

        return arr
        