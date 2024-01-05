from collections import defaultdict

def sortingApproach(strs: [str]) -> [[str]]:
    res = defaultdict(list)
    for s in strs:
        # sorted returns an array of characters in sorted order
        # "".join converts that back into a string
        res["".join(sorted(s))].append(s)
    return res.values()

# categories words by their frequency in a count array, then hashes using that: the value is list of values hashed to that count array (tuple in python since arrays aren't hashable)
def groupAnagrams(strs: [str]) -> [[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord("a")] += 1
        
        res[tuple(count)].append(s)
    
    return res.values()


