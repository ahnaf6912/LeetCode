class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        new_list = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                new_list.append(s[i])
            if len(s) < 2:
                return False
            else:
                if len(new_list) == 0:
                    return False
                if s[i] == ")" and new_list.pop() != "(":
                    return False
                if s[i] == "]" and new_list.pop() != "[":
                    return False
                if s[i] == "}" and new_list.pop() != "{":
                    return False
        if len(new_list) == 0:
            return True
        else:
            return False