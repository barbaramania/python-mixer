#Un-optimized bubble method for the following task:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):  
        length = len(nums)
        x = 0
        found_match = False
        while x <= length :
            j=x+1
            while j<=(length-1):
                    if target == nums[j] + nums[x]:
                        found_match = True
                        break 
                    j+=1
            if found_match == True:
                break 
            x+=1
        return x, j

