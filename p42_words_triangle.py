import math

characters = ['','A','B','C','D','E','F','G','H','I','J','K'
,'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def sum_word_character(word):
    s = 0
    for c in word:
        s += characters.index(c)
    return s

"""
for testing is triangle number we should solve following problem according to n
n(n+1)/2=x
if we solve this problem we get these answers:
    n = (-1 + sqrt(1 + 8x))/2    , n = (-1 - sqrt(1 + 8x))/2
in these answers if sqrt(1 + 8x)    [Delta] was integer the number is triangle number
"""
def is_triangle_number(n):
    return 1 if math.ceil(math.sqrt(1 + 8 * n)) == math.sqrt(1 + 8 * n) else 0

f = open("p042_words.txt","r")
words = f.read()
words_list = words.split("\",\"")
words_list[0] = words_list[0].replace("\"",'')
words_list[len(words_list) - 1]=words_list[len(words_list) - 1].replace("\"",'')

s_tot = 0
for x in words_list:
    if(is_triangle_number(sum_word_character(x)) > 0):
        s_tot += 1
        print(x)

print(s_tot)
