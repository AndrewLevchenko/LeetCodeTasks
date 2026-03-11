class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        minimal = min(nums)

        d = {}
        for i, num in enumerate(nums):
            if minimal + num <= target:
                if num in d and target == 2 * num:
                    return [min(d[num], i), max(d[num], i)]
                else:
                    d[num] = i

        for num1 in d.keys():
            num2 = target - num1
            if num1 != num2 and num2 in d.keys():
                return [min(d[num1], d[num2]), max(d[num1], d[num2])]