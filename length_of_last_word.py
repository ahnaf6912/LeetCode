class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = []
        for word in s.split():
            word_list.append(word)
        return len(word_list[len(word_list) - 1])