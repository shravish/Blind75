# Without class

from collections import defaultdict

def group_anagrams(strs):
      # A dictionary that automatically creates a new list entry for each new key
      anagrams = defaultdict(list)
      # Iterate through each string in the provided list
      for s in strs:
          # Sort the string to create a key for the anagrams
          # Since sorted returns a list of characters, join them to form a string
          key = "".join(sorted(s))
          # Append the original string to the list of anagrams with the same key
          anagrams[key].append(s)
          # Convert the dictionary values to a list and return it
      return list(anagrams.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(group_anagrams(strs))
# output: [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]

strs = ["x"]
print(group_anagrams(strs))
# output: [['x']]

strs = [""]
print(group_anagrams(strs))
# output: [['']]

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# With class

from collections import defaultdict

class Solution:
   def group_anagrams(self, strs):
      # A dictionary that automatically creates a new list entry for each new key
      anagrams = defaultdict(list)
      # Iterate through each string in the provided list
      for s in strs:
          # Sort the string to create a key for the anagrams
          # Since sorted returns a list of characters, join them to form a string
          key = "".join(sorted(s))
          # Append the original string to the list of anagrams with the same key
          anagrams[key].append(s)
          # Convert the dictionary values to a list and return it
      return list(anagrams.values())

obj = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(obj.group_anagrams(strs))
# output: [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]
