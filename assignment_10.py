#question1

def non_alphabet(a):
    result = 0
    for char in a:
        if a.isalpha():
            result += 1
    return result

print(non_alphabet("H3ll0_Wor!ld#2025"))

#question2
# words = 'cat dog dog bird cat cat'
# def most_frequent_word(sentence):
#     words = sentence.split()
#     count = 0
#     for word in words:
def most_frequent_word(sentence):
    words = sentence.split()
    max_count = 0
    frequent_word = ''
    for word in words:
        count = words.count(word)
        if count > max_count:
            max_count = count
            frequent_word = word
    return frequent_word

print(most_frequent_word('cat dog dog bird cat cat'))

#question3
word = 'crypt'
vowels = ['a','e','i','o','u']
def vowel_index(index):
    for wor in word:
        if vowels == word:
            print("match")
        else:
            return -1

print(vowel_index(word))

#question4
#word = 'education'
def move_vowels_to_end(a):
    vowels = 'aeiouAEIOU'
    consonants = ''
    vowel_part = ''
    for char in a:
        if char in vowels:
            vowel_part += char
        else:
            consonants += char
    return consonants + vowel_part

print(move_vowels_to_end('education'))

#question5
a = 'banana'
frequency = {}
for char in a:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)

#question6
vowels = 'aeiou'
sentence = 'hello world'
result = ''
for char in sentence:
    if char in vowels:
        result += char.upper()
    else:
        result += char

print(result)

#question7
digits = '12345'
for char in digits:
    if 1 < 2 < 3 < 4 < 5:
        print('true')

#question8
line = 'This is a beautiful sunny day'
words = line.split()
count = 0
for word in words:
    if len(word) > 4 :
        count += 1
print(count)    

#question11
# sentence = 'open ai builds tools'
# words = sentence.split()

# for word in words:
#     if True:
#         words.reverse()
#     else:
#         pass

# print(sentence)
s = 'open ai builds tools'
words = s.split()
reversed_words = words[::-1]
result = ''.join(reversed_words)
print(result)

#question12
x = 'a1b2c3'
result = x[::2]
print(result)



        




