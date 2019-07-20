class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""

        chars = self.getChars(words)

        indegrees , posts = self.helper(words, chars)

        queue = []
        for char in chars:
            if indegrees[char]==0 :
                queue.append(char)

        index = 0
        while index<len(queue):
            top = queue[index]
            for post in posts[top]:
                indegrees[post] -= 1
                if indegrees[post]==0:
                    queue.append(post)
            index += 1

        if len(queue) == len(chars):
            return ''.join(queue)
        return ''


    def getChars(self, words):
        chars = set()
        for word in words:
            for char in word:
                chars.add(char)
        return chars

    def helper(self, words, chars):
        indegrees , posts = {}, {}
        for char in chars:
            indegrees[char] = 0
            posts[char] = []

        for i in range(1, len(words)):
            word1 , word2 = words[i-1], words[i]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    indegrees[word2[j]] += 1
                    posts[word1[j]].append(word2[j])
                    break

        return indegrees, posts

##################################################################################
# Topological Sorting
#     1. find indegrees and posts items 
#     2. bfs traverse
#
##################################################################################
