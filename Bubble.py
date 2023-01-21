# Bubble Sort

def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                
                print(nums)

nums = [31, 18, 14, 53, 54, 98, 93, 92, 74, 69]
sort(nums)

print(nums)

# Reference: https://youtu.be/Vca808JTbI8
