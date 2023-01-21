
# Insertion Sort

def sort(nums):
    for i in range(1, len(nums)):
        anchor = nums[i]
        j = i - 1
        while j>=0 and anchor < nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = anchor
        
        print(nums)

nums = [31, 18, 14, 53, 54, 98, 93, 92, 74, 69]
sort(nums)

print(nums)

# Reference: https://youtu.be/K0zTIF3rm9s