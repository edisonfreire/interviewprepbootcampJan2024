# Valid anagram
# used two dictionaries
# O(n) time, O(n) space
def firstApproach(s: str, t: str) -> bool:
        map1 = {}
        for char in s:
            if char not in map1:
                map1[char] = 1
            else:
                map1[char] += 1

        map2 = {}
        for char in t:
            if char not in map2:
                map2[char] = 1
            else:
                map2[char] += 1

        return map1 == map2

# used one dictionary, same complexity
# O(s+t) time, O(s+t) space
def secondApproach(s: str, t: str) -> bool:
        map1 = {} # O(s + t) space
        for char in s: # O(s)
            if char not in map1:
                map1[char] = 1
            else:
                map1[char] += 1

        for char in t: # O(t)
            if char not in map1:
                return False
            else:
                map1[char] -= 1

        # checks if anagram every value should be 0 since every addition from s should have a subtraction from t
        for x in map1.values(): # O(s + t)
            if x != 0:
                return False
        return True

# counter library
from collections import Counter
def thirdApproach(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)