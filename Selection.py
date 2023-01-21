
# Selection Sort

def sort(nums):

    for i in range(9):
        minpos = i
        for j in range(i,10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [31, 18, 14, 53, 54, 98, 93, 92, 74, 69]
sort(nums)

print(nums)


# Reference : https://youtu.be/5KjapFQNxUo