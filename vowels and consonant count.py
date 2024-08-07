def count_vowels_consonants(s):
    vowels = 'aeiou'
    s = s.lower()
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha() and char not in vowels:
            consonant_count += 1
        elif char==" ":
            pass
    return {'vowels': vowel_count, 'consonants': consonant_count}
str=input("Enter a string:")
print(count_vowels_consonants(str))
