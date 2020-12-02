lines = open("input.txt","r").readlines()
nums = list(map(int, lines))

for i, num in enumerate(nums):
    for j in range(i, len(nums)):
        if num + nums[j] == 2020:
            print(num * nums[j])
