nums = [4,1,2,1,2]
result = 0
for i in range(len(nums)):
    result = result^nums[i]
    print(result)