text = input("Enter text: ")

char_count = len(text)
word_count = len(text.split())

vowel_count = 0
for ch in text.lower():
    if ch in "aeiou":
        vowel_count += 1

print("Characters:", char_count)
print("Words:", word_count)
print("Vowels:", vowel_count)
print("Uppercase:", text.upper())
