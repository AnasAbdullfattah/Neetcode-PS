class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        n = len(s)
        left = 0
        right = n - 1
        if n <= 1:
            return True

        while left < right:
            if not s[right].isalnum():
                right = right - 1
                continue
            if not s[left].isalnum():
                left = left + 1
                continue
            if s[left] != s[right]:
                return False
            else:
                left = left + 1
                right = right - 1
        return True


x = Solution()
a = x.isPalindrome("A man, a plan, a canal: Panama")
print(a)