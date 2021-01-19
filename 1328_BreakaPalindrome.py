class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        # at the 1st HALF, change the 1st non-"a" to a 
        for i in range(n//2):
            if palindrome[i] != 'a':
                return palindrome[:i]+'a'+palindrome[i+1:]
                
        # all "a" then change the first one to b
        return palindrome[0:-1]+"b"
