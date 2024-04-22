"""
Given a string s, find the length of the longest substring without repeating characters

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring
"""
class Solution:
    def find_sub(self, in_s: str):
        unique = {}
        count = 0
        for c in in_s:
            if not unique:
                unique[c] = True
                count += 1
            elif c not in unique:
                unique[c] = True
                count += 1
            else:
                break
        return count
            
    def lengthOfLongestSubstring(self, s: str):
        if not s:
            return 0
        count = 0
        most = 0
        index = 0
        while index < len(s):
            count = self.find_sub(s[index::])
            if count > most:
                most = count
            index += 1
        return most

