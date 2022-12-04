# 2256. Minimum Average Difference
# instead of using dictionary for index of element and value, use enumerate - space better
# compare minimum value and the average value difference at the same time - time saving
nums = [1,2,3,4,5,6,7,8,9,0]
sum_of_all_numbers = 0
for num in nums:
    sum_of_all_numbers += num  # find the sum of all numbers
max_const_diff = float("inf")  # min diff
res = 0
temp_sum = 0  # sum of numbers for that index
for i, num in enumerate(nums):
    temp_sum += num
    diff1 = int(temp_sum/(i+1))
    if (i == len(nums)-1):  # last case
        diff2 = 0
    else:
        diff2 = int((sum_of_all_numbers-temp_sum)/(len(nums)-i-1))
    if (max_const_diff > abs(diff1-diff2)):
        res = i
        max_const_diff = min(max_const_diff, abs(diff1-diff2))
print(res) #min index