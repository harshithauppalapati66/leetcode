class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str=str(x)
        if x_str == x_str[::-1]:
            print('true')
            return True
        else:
            print('false')
            return False
