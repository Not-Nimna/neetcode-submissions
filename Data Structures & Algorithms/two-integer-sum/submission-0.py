class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        hasmap = {}
        res = []
        for idx, val in enumerate(nums):
            diff = target - val

            if diff in hasmap:
                res.append(hasmap[diff])
                res.append(idx)
                
                return res
            hasmap[val] = idx

