import math

characters = ['','A','B','C','D','E','F','G','H','I','J','K'
,'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def word_scores(word):
    s = 0
    for c in word:
        s += characters.index(c)
    return s

f = open("p022_names.txt")
words = f.read()
words_list = words.split("\",\"")
words_list[0] = words_list[0].replace("\"",'')
words_list[len(words_list) - 1]=words_list[len(words_list) - 1].replace("\"",'')

words_list.sort()
s_tot = 0
xi = 1
for x in words_list:
    s_tot += word_scores(x) * xi
    xi += 1

print(s_tot)
