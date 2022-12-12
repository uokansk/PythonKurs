"""
в файле натуральные числа записанные через пробел и среди их нет числа,
что бы выполнить условие перепиши все числа подряд.
"""

# num = open('listNumbers.txt')
# numbers = num.read()
# print(numbers)
#
# numbersList = numbers.split()
# print(numbersList)

with open('listNumbers.txt', 'r') as f:
    nums = list(map(int, f.read().split()))
print(nums)

for i in range(1, len(nums)):
    if nums[i] - nums[i - 1] > 1:
        nums.insert(i, nums[i - 1] + 1)

print(nums)

data = open('listNumbers.txt', 'w')
data.write(' '.join(list(map(str, nums))))
data.close()
