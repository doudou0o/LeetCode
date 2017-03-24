#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        wordsNum = {}
        for w in words:
            wordsNum[w] = wordsNum.get(w,0)+1

        wordLen = len(words[0])

        ansPos = []
        window = [0,0]
        wordsNumTemp = {}
        wordsDictTemp = {}
        for i in range(wordLen):
            window = [i,0]
            wordsNumTemp.clear()
            wordsDictTemp.clear()
            for j in range(i, len(s), wordLen):
                word = s[j:j+wordLen]
                if word not in wordsNum:
                    wordsNumTemp.clear()
                    wordsDictTemp.clear()
                    window = [j+wordLen, j+wordLen]
                else:
                    if word not in wordsNumTemp or wordsNumTemp[word] < wordsNum[word] or (word in wordsDictTemp and wordsDictTemp[word][0] < window[0]): # 正常加入窗口
                        if word not in wordsNumTemp or  wordsNumTemp[word] < wordsNum[word]:
                            wordsNumTemp[word] = wordsNumTemp.get(word, 0) + 1
                            wordsDictTemp[word] = wordsDictTemp.get(word, [])
                            wordsDictTemp[word].append(j)
                            window[1] = j+wordLen
                        elif wordsDictTemp[word][0] < window[0]:
                            wordsDictTemp[word] = wordsDictTemp[word][1:]
                            wordsDictTemp[word].append(j)
                            window[1] = j+wordLen
                    else: # 需要窗口变化
                        window[0] = wordsDictTemp[word][0] + wordLen
                        window[1] = j+wordLen
                        wordsDictTemp[word] = wordsDictTemp[word][1:]
                        wordsDictTemp[word].append(j)
                    if window[1]-window[0] == len(words)*wordLen:
                        ansPos.append(window[0])
        return ansPos



if __name__ == '__main__':
    print Solution().findSubstring("ibarfoobarthefoobarman", ["foo", "bar"])
    print Solution().findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])
    print Solution().findSubstring("aaaaaaaa", ["aa","aa","aa"])


