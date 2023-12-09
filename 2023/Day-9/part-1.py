s = 0
with open("input") as f:
    for line in f:
        diffs = []
        nums = [int(x) for x in line.split(" ")]

        diffs.append(nums[-1])
        while nums.count(0) != len(nums):
            for i in range(len(nums) - 1):
                nums[i] = nums[i + 1] - nums[i]

            nums.pop(-1)
            diffs.append(nums[-1])

        s += sum(diffs)

print(s)

