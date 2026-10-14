class Solution(object):
    def isPalindrome(self, s):
        cleaned = [char.lower() for char in s if char.isalnum()]
        return cleaned == cleaned[::-1]