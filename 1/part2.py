lines = open("input.txt","r").readlines()
nums = list(map(int, lines))

for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            if nums[i] + nums[j] + nums[k] == 2020:
                print(nums[i] * nums[j] * nums[k])
