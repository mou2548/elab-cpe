VOWELS = "aeiou"
vowel = []
consonant = []

strings = input("Enter a string: ").split()

for string in strings:
    for c in string.lower():
        if c in VOWELS:
            if c not in vowel:
                vowel.append(c)
        elif c not in consonant and c.isalpha():
            consonant.append(c)

print("Unique vowels: ", vowel)
print("Unique consonants: ", consonant)
            
