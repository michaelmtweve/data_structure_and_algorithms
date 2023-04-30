target =int(input('enter the target value(sum)\n')) #prompting the user to enter the target value
nums = [1, 3, 6, 9, 12, 3, 8, 24, 89, 35] #list declaring
def two_indices(nums, target):
    n = len(nums)
    for x in range(0, n):
        for y in range(0, n):
            if nums[x] + nums[y] == target:
                u = x 
                v = y
    print(("The indices of integers are:")+"[", u, ",", v, "]")
    


two_indices(nums, target);