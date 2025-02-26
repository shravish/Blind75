def containsDuplicate(nums):
    # Create an empty set to store unique elements
    unique_set = set()

    # Iterate through the array
    for num in nums:
        # If the element is already in the set, it's a duplicate
        if num in unique_set:
            return True
        # Otherwise, add the element to the set
        unique_set.add(num)

    # If the loop completes without returning, there are no duplicates
    return False
nums = [1,2,3,4,5]
print(containsDuplicate(nums))   
# output: False
nums = [1,2,3,3]
print(containsDuplicate(nums))  
# output: True
