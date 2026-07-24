class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_number = ''
        for i in range(1, len(str((x))) + 1):
            new_number = new_number + str(x)[len(str(x)) - i]
        if new_number == str(x):
            return True
        else:
            return False