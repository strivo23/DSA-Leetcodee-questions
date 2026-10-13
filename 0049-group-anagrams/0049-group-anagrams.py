class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = {}
        for s in strs:
            sorted_key = "".join(sorted(s))

            if sorted_key not in anagram_map:
                anagram_map[sorted_key]=[]
            anagram_map[sorted_key].append(s)
        return list(anagram_map.values())