def twoSum(nums: list[int], target: int) -> list[int]:
        # Keep track of visited number and its index position. E.g. {2:0}
        visited = {}
        numsLen = len(nums)
        for currIdx in range(numsLen):
            currNum = nums[currIdx]
            remaining = target - currNum
            # Did we already visit a number that the current number can add up to the target?
            if remaining in visited:
                visitedIdx = visited[remaining]
                return [visitedIdx, currIdx]
            else:
                visited[currNum] = currIdx
                
print(twoSum([1, 2, 7, 4], 5))
# output: [0, 3]
print(twoSum([3, 4, 5, 6], 7))
# output: [0, 1]
