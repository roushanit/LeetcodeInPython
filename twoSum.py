#using hashmap to make it this code optimal
def twoSum(nums, target):
    hashmap = {}
#using enumerate to get index & value details of number
    for i, num in enumerate(nums):
        diff = target - num

        if diff in hashmap:
            return [hashmap[diff], i]

        hashmap[num] = i
print(twoSum([2,7,11,15], 9))        
