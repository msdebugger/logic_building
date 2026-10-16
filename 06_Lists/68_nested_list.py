"""
Q68: Create a 3x3 matrix (a nested list) and then use nested loops to calculate and print the sum of all its elements. Example: matrix=[[1,2,3],[4,5,6],[7,8,9]] -> sum is 45.

"""
nums = [[1,2,3],[4,5,6],[7,8,9]]

result = 0

for i in range(len(nums)):
    for j in range(len(nums[i])):
        result = result + nums[i][j]
    
print(f"Sum is: {result}")        