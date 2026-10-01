class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        ss = s[:k]
        curr_count = sum(1 for char in s[:k] if char in vowels)
        max_count = curr_count
        if max_count == k:
            return k
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr_count += 1
            if s[i - k] in vowels:
                curr_count -= 1
            max_count = max(max_count, curr_count)

            if max_count == k:
                return k
        return max_count