class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum(): # .isalnum(): A built-in Python method that returns True if a character is a letter (a-z, A-Z) or a number (0-9), and False if it's a space, comma, colon, exclamation mark, etc.
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
