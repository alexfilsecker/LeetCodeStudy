from typing import List

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if num in hash:
                return True
            else:
                hash[num] = True
        
        return False
        

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))