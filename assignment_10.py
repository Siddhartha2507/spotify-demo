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


        






