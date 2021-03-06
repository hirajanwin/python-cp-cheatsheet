"""
time: n
space: n
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1} 
        rtn, total = 0, 0
        for n in nums:
            total += n
            rtn += mp.get(total - k, 0)
            mp[total] = mp.get(total, 0) + 1
        return rtn

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.Counter()
        count[0] = 1
        ans = total = 0
        for x in nums:
            total += x
            ans += count[total-k]
            count[total] += 1
        return ans