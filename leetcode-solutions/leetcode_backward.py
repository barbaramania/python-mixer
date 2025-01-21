#Un-optimized bubble method for the following task:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# class Solution(object):
#     def twoSum(self, nums, target):  
#         length = len(nums)
#         x = 0
#         found_match = False
#         while x <= length :
#             j=x+1
#             while j<=(length-1):
#                     if target == nums[j] + nums[x]:
#                         found_match = True
#                         break 
#                     j+=1
#             if found_match == True:
#                 break 
#             x+=1
#         return x, j


#Some-optimized 
nums = [1, 3, 4, 7, 8, 9]
target = 13
exit_key = False
for x in range(0,len(nums)):
    for y in range(x+1,len(nums)):
        if target == nums[x] + nums[y]:
            exit_key = True
            break
    if exit_key:
        break
print(f"Found pair: nums[{x}] = {nums[x]}, nums[{y}] = {nums[y]}")




# # not working
# # nums = [1, 3, 4, 7]
# # for x in nums:
# #     print(nums[x])
# # output is 3 and 7, as x = 1(as the first element) -> 3 and x = 3(as a second element) -> 7 and then an error