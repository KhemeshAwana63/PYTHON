class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind = 0
        ind2 = ind + 1
        for val in nums:
            store = val
            nums2 = nums[ind+1:]
            for val2 in nums2:
                store2 = val2
                if store + store2 == target:
                    print(f'{ind} and {ind2} give the sum {target}')
                    break
                ind2 += 1
            ind += 1
            ind2 = ind + 1
            if store + val2 == target:
                break

"""this is my first ever leetcode problem and as you can see my program
did not run and has so many errors but i will learn about them and 
improve them"""