class Solution(object):
    def isPalindrome(self, x):
       to_str = str(x)
       reverse_to_str = to_str[::-1]
       #y = int(reverse_to_str)
       if to_str == reverse_to_str:
            return True
       else:
            return False
