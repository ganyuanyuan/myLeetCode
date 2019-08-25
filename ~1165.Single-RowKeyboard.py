class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        mapping = {}
        for i, char in enumerate(keyboard):
            mapping[char] = i
        ans = 0
        for i in range(len(word)):
            if i == 0 :
                ans += mapping[word[i]]
            else:
                ans += abs(mapping[word[i]]-mapping[word[i-1]])

        return ans 
