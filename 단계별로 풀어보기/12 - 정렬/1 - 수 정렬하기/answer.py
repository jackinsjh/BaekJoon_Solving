numOfNums = int(input())
nums = list()
for i in range(numOfNums):
    nums.append(int(input()))
nums.sort()
for i in range(numOfNums):
    print(nums[i])